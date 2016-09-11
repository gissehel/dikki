#!/usr/bin/env python
# coding: utf-8

from .tools import get_short_id

class Image(object):
    def __init__(self, raw_image=None, image_info=None, tids=None):
        self._raw_image = raw_image
        self.tids = None
        self.tid = None
        self.parent_tid = None
        self.parent_lid = None
        self.created = 0
        self.virtual_size = None
        self.tags = []

        if raw_image is None :
            self.lid = '<no image>'
            self.sid = '<no image>'
            self.name = '<no image>'
            if tids is not None:
                self.tids = tids
                if len(self.tids)>0:
                    self.sid = '(L:{})'.format(self.tids[-1])
        else:
            self.lid = raw_image['Id']
            lid = self.lid
            self.sid = get_short_id(self.lid)
            self.name = '"%s"' % (self.sid,)
            if raw_image['RepoTags'] is not None:
                for tag in raw_image['RepoTags']:
                    if tag != u'<none>:<none>':
                        self.tags.append(tag)
            self.parent_lid = raw_image['ParentId']
            self.created = raw_image['Created']
            self.virtual_size = raw_image['VirtualSize']
            self.size = raw_image['Size']

            if image_info is not None:
                self.tids = list(get_short_id(layer_id) for layer_id in image_info['RootFS']['Layers'])

        if self.tids is not None:
            self.tid = ','.join(self.tids)
            self.parent_tid = ','.join(self.tids[:-1])
            if len(self.parent_tid) == 0:
                self.parent_tid = None
        else:
            self.tid = None
            self.parent_tid = None
        self.is_running = False
        self.is_stopped = False
        self.is_child_stop_or_running = False
        self.children = []
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def is_important(self):
        return len(self.tags)>0

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

    def get_created(self):
        if self.created > 0:
            return self.created
        if len(self.children)>0:
            return min(child.get_created() for child in self.children)
        return 0

