#!/usr/bin/env python
# coding: utf-8

class Image(object):
    def __init__(self, raw_image=None):
        self._raw_image = raw_image
        if raw_image is None :
            self.lid = ''
            self.sid = ''
            self.name = 'base'
            self.tags = []
            self.parent_lid = None
            self.created = None
            self.is_root = True
        else:
            self.lid = raw_image['Id']
            self.sid = self.lid[:12]
            self.name = '"%s"' % (self.sid,)
            self.tags = []
            for tag in raw_image['RepoTags']:
                if tag != u'<none>:<none>':
                    self.tags.append(tag)
            self.parent_lid = raw_image['ParentId']
            self.created = raw_image['Created']
            self.virtual_size = raw_image['VirtualSize']
            self.size = raw_image['Size']
            self.is_root = False
        self.children = []
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def is_important(self):
        return len(self.tags)>0 or len(self.children)!=1

