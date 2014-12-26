#!/usr/bin/env python
# coding: utf-8

class Container(object):
    def __init__(self, raw_container, raw_container_info):
        self._raw_container = raw_container
        self.lid = raw_container['Id']
        self.sid = self.lid[:12]
        self.name = '"%s"' % (self.sid,)
        
        self.names = []
        for name in raw_container['Names']:
            if name.startswith('/'):
                self.names.append(name[1:])
            else:
                raise Exception('Unexpected container name not starting by / : [%s] (Id:%s)' % (name,self.sid))
        self.created = raw_container['Created']
        self.image = raw_container['Image']
        self.ports = raw_container['Ports']
        self.status = raw_container['Status']
        self.tags = [None]
        self.running = raw_container_info['State']['Running']
        self.command = raw_container_info['Path']
        self.is_important = self.running

    #def set_parent(self, parent):
    #    self.parent = parent
    #    parent.children.append(self)


