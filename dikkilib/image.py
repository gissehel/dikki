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
        self.is_running = False
        self.is_stopped = False
        self.is_child_stop_or_running = False
        self.children = []
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def is_important(self):
        return len(self.tags)>0 or len(self.children)!=1 or (self.parent is None)

    def set_running(self):
        self.is_running = True
        self.is_child_stop_or_running = True

    def set_stopped(self):
        self.is_stopped = True
        self.is_child_stop_or_running = True

    def set_child_stop_or_running(self):
        self.is_child_stop_or_running = True

    def get_run_status(self):
        if self.is_running:
            return '*'
        elif self.is_stopped:
            return '+'
        elif self.is_child_stop_or_running:
            return '-'
        return ' '

