#!/usr/bin/env python3
# coding: utf-8

from itertools import chain
from .attributable import Attributable
from .tools import human_readable_bytes
from .tools import write_tree
from .tools import format_time
from .tools import format_time_rel
from .tools import format_ports
from .tools import format_bool
from .tools import get_tree_prefix
from .tools import wrap_handle

class Containers(Attributable):
    def __init__(self, container_class, container_walker_class, raw_docker) :
        self._Container = container_class
        self._ContainerWalker = container_walker_class
        self._raw_docker = raw_docker
        self._by_names = {}
        self._container_walker = None

    def get_walking_object(self):
        return self._container_walker.walk()

    def load_containers(self):
        containers = [ self._Container(raw_container, self._raw_docker.get_container_info(raw_container['Id'])) for raw_container in self._raw_docker.get_containers() ]

        self._by_names = {}
        self._container_walker = self._ContainerWalker(containers)

    _attribut_getter = {
        'id': (lambda walker_item: walker_item.item.sid),
        'longid': (lambda walker_item: walker_item.item.lid),
        'running': (lambda walker_item: format_bool(walker_item.item.running)),
        'created': (lambda walker_item: format_time(walker_item.item.created)),
        'createdrel': (lambda walker_item: format_time_rel(walker_item.item.created)),
        'command': (lambda walker_item: ('"%s"' % (walker_item.item.command,))[:20]),
        'status': (lambda walker_item: walker_item.item.status),
        'image': (lambda walker_item: walker_item.item.image),
        'imageid': (lambda walker_item: walker_item.item.imagesid),
        'ports': (lambda walker_item: format_ports(walker_item.item.ports)),
        'names': (lambda walker_item, sep=', ': sep.join(walker_item.item.names)),
        'name': (lambda walker_item: walker_item.item.name),
        'ip': (lambda walker_item: walker_item.item.ip),
        'ipv6': (lambda walker_item: walker_item.item.ipv6),
        'mac': (lambda walker_item: walker_item.item.mac),
        }

    def write_result(self, handle, all=False, output=None, mode_ascii=False, data_format=None):
        self.load_containers()
        handle_wrapped = wrap_handle(handle,'utf-8')
        walking = self.get_walking_object()
        if output=='tree':
            if data_format is None:
                if mode_compact:
                    data_format = 'id/" [ "tags" ]"'
                else:
                    data_format = 'id/"Virtual Size: "vsize/"Tags: "tags<, >'
            formatter = self.get_tree_formatter(data_format)
            write_tree(handle_wrapped, walking, formatter, mode_ascii)
        elif output=='digraph':
            self.write_digraph(handle_wrapped, walking, as_point=as_point)
        elif output=='table':
            if data_format is None:
                data_format = 'id/imageid/image/command/createdrel" ago"#created/status/ports/name'
            self.write_table(handle_wrapped, walking, all=all, data_format=data_format)
        elif output=='treetable':
            if data_format is None:
                data_format = 'id/imageid/image/command/createdrel" ago"#created/status/ports/name'
            self.write_treetable(handle_wrapped, walking, all=all, data_format=data_format, mode_ascii=mode_ascii)

    def is_important(self):
        return True
