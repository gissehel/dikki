#!/usr/bin/env python3
# coding: utf-8

from .tools import get_short_id

class Container(object):
    def __init__(self, raw_container, raw_container_info):
        self._raw_container = raw_container
        self.lid = raw_container['Id']
        self.sid = get_short_id(self.lid)
        self.name = '"%s"' % (self.sid,)
        
        self.names = []
        if 'Names' in raw_container:
            for name in raw_container['Names']:
                self.names.append(self.get_container_name(name))
        if 'Name' in raw_container_info:
            self.name = self.get_container_name(raw_container_info['Name'])
        self.created = raw_container['Created']
        self.image = raw_container['Image']
        if self.image.startswith('sha256:'):
            self.image = get_short_id(self.image)
            if 'Config' in raw_container_info and 'Image' in raw_container_info['Config']:
                self.image = '{id} (was {name})'.format(id=self.image, name=raw_container_info['Config']['Image'])
        self.ports = raw_container['Ports']
        self.status = raw_container['Status']
        self.tags = [None]
        self.imagelid = raw_container_info['Image']
        self.imagesid = get_short_id(self.imagelid)
        self.running = raw_container_info['State']['Running']
        self.command = raw_container_info['Path']
        self.ip = raw_container_info['NetworkSettings']['IPAddress']
        self.ipv6 = raw_container_info['NetworkSettings']['LinkLocalIPv6Address']
        self.mac = raw_container_info['NetworkSettings']['MacAddress']
        self.is_important = self.running

    def get_container_name(self, rawname):
        if rawname.startswith('/'):
            return rawname[1:]
        else:
            raise Exception('Unexpected container name not starting by / : [{rawname}] (Id:{id})'.format(rawname=rawname,id=self.sid))


    #def set_parent(self, parent):
    #    self.parent = parent
    #    parent.children.append(self)


