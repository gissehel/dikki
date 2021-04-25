#!/usr/bin/env python3
# coding: utf-8

from .tools import get_short_id

def get_best_value_from_labels(labels, label_best_keys):
    for label_best_key in label_best_keys:
        if label_best_key in labels:
            return labels[label_best_key]
    return None

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
        self.title = None
        self.version = None

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
                    if tag != '<none>:<none>':
                        self.tags.append(tag)
            self.parent_lid = raw_image['ParentId']
            self.created = raw_image['Created']
            self.virtual_size = raw_image['VirtualSize']
            self.size = raw_image['Size']
            if 'Labels' in raw_image and raw_image['Labels'] is not None:
                labels = raw_image['Labels']
                self.title = get_best_value_from_labels(labels, ['org.opencontainers.image.title', 'org.label-schema.name'])
                self.version = get_best_value_from_labels(labels, ['org.opencontainers.image.version', 'org.label-schema.version', 'Version'])

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

