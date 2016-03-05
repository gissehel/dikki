#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from itertools import chain
from .attributable import Attributable
from .tools import human_readable_bytes
from .tools import write_tree
from .tools import format_time
from .tools import format_time_rel
from .tools import wrap_handle

class Images(Attributable):
    def __init__(self, image_class, image_walker_class, container_class, raw_docker) :
        self._by_id = {}
        self._by_tag = {}
        self._Image = image_class
        self._ImageWalker = image_walker_class
        self._Container = container_class
        self._raw_docker = raw_docker
        self._image_walker = None
        

    def find_image(self, tag):
        if tag == '':
            return None
        xtag = tag
        if ':' not in xtag:
            xtag = xtag + u':latest'
        if xtag in self._by_tag:
            return [ self._by_tag[xtag] ]
        ids = [xid for xid in self._by_id if xid.lower().startswith(tag)]
        if len(ids) == 0:
            raise Exception(u'No image found (%r)' % (tag,))
        else:
            return [ self._by_id[id] for id in ids ]

    def write_digraph(self, handle=None, walking=None, as_point=True):
        handle.write(u'digraph docker {\n')
        for walker_item, prefix in walking:
            image = walker_item.item
            children = [ walker_child.item for walker_child in walker_item.children ]
            for child in children:
                handle.write(u' %s -> %s\n' % (image.name, child.name))
            if len(image.tags)>0:
                handle.write(u' %s [label="%s",shape=box,fillcolor="paleturquoise",style="filled,rounded"];\n' % (image.name, u'\\n'.join([image.sid] + sorted(image.tags))))
            elif as_point:
                handle.write(u' %s [label="%s",shape="point"];\n' % (image.name, ''))
        handle.write(u'}\n')
        
    def classic_format_tree_line(self, handle, walker_item):
        handle.write(walker_item.item.sid)
        handle.write(u' Virtual Size: ')
        handle.write(human_readable_bytes(walker_item.item.virtual_size))
        if len(walker_item.item.tags)>0:
            handle.write(u' Tags: ' + ', '.join(walker_item.item.tags))

    def compact_format_tree_line(self, handle, walker_item):
        handle.write(walker_item.item.sid)
        if len(walker_item.item.tags)>0:
            handle.write(u'     ' + u'  '.join(walker_item.item.tags))

    def get_tree_formatter(self, generic_format):
        def tree_formatter(handle, walker_item):
            for count, value in enumerate(self.get_attributes(walker_item, generic_format.split(u'/'))):
                if count > 0 and len(value) > 0:
                    handle.write(u' ')
                handle.write(value)
        return tree_formatter

    def get_walking_object(self, tag=u'', all=False):
        ref_images = self.find_image(tag)
        walker = self._image_walker if all else self._important_image_walker

        if ref_images is None:
            walking = walker.walk()
        else:
            walking = chain.from_iterable(walker.get_walker_item(ref_image).walk() for ref_image in sorted(ref_images, key=lambda image:-image.created))

        return walking

    def load_images(self):
        images = [ self._Image(raw_image) for raw_image in self._raw_docker.get_images() ]

        self._by_id = {}
        self._by_tag = {}
        self._image_walker = self._ImageWalker()
        self._important_image_walker = self._ImageWalker()

        for image in images :
            self._by_id[image.lid] = image
            for tag in image.tags:
                self._by_tag[tag] = image

        for image in images :
            if image.parent_lid in self._by_id:
                image.set_parent(self._by_id[image.parent_lid])
                self._image_walker.set_parent(image, self._by_id[image.parent_lid])
            else:
                self._image_walker.get_walker_item(image)

        self._image_walker.froze_walker()
        important_parents = {}
        for walker_item, prefix in self._image_walker.walk():
            image = walker_item.item
            if walker_item.parent is None:
                if image.is_important():
                    self._important_image_walker.get_walker_item(image)
            else:
                parent = walker_item.parent.item
                if parent.is_important():
                    if image.is_important():
                        self._important_image_walker.set_parent(image, parent)
                    important_parents[image] = parent
                else:
                    if parent in important_parents :
                        if image.is_important():
                            self._important_image_walker.set_parent(image, important_parents[parent])
                        important_parents[image] = important_parents[parent]
        self._important_image_walker.froze_walker()

    def load_status(self):
        containers = [ self._Container(raw_container, self._raw_docker.get_container_info(raw_container['Id'])) for raw_container in self._raw_docker.get_containers() ]
        for container in containers:
            if container.imagelid in self._by_id:
                if container.running:
                    self._by_id[container.imagelid].set_running()
                else:
                    self._by_id[container.imagelid].set_stopped()
                loop_image = self._by_id[container.imagelid]
                while loop_image is not None:
                    loop_image.set_child_stop_or_running()
                    loop_image = loop_image.parent

    _attribut_getter = {
        'id': (lambda walker_item: walker_item.item.sid),
        'longid': (lambda walker_item: walker_item.item.lid),
        'tags': (lambda walker_item,sep=' ': sep.join(sorted(walker_item.item.tags))),
        'vsize': (lambda walker_item: human_readable_bytes(walker_item.item.virtual_size)),
        'diffsize': (lambda walker_item: human_readable_bytes(walker_item.item.virtual_size-(walker_item.parent.item.virtual_size if walker_item.parent is not None else 0))),
        'size': (lambda walker_item: human_readable_bytes(walker_item.item.size)),
        'parentid': (lambda walker_item: (walker_item.parent.item.sid if walker_item.parent is not None else '')),
        'created': (lambda walker_item: format_time(walker_item.item.created)),
        'createdrel': (lambda walker_item: format_time_rel(walker_item.item.created)),
        'status': (lambda walker_item: walker_item.item.get_run_status())
        }

    def write_result(self, handle, tag=u'', all=False, as_point=True, output=None, mode_compact=False, mode_ascii=False, data_format=None):
        self.load_images()
        self.load_status()
        handle_wrapped = wrap_handle(handle,'utf-8')
        walking = self.get_walking_object(tag, all=all)
        if output==u'tree':
            if data_format is None:
                if mode_compact:
                    data_format = u'id/" [ "tags" ]"'
                else:
                    data_format = u'id/"Virtual Size: "vsize/"Tags: "tags<, >'
            formatter = self.get_tree_formatter(data_format)
            write_tree(handle_wrapped, walking, formatter, mode_ascii)
        elif output==u'digraph':
            self.write_digraph(handle_wrapped, walking, as_point=as_point)
        elif output==u'table':
            if data_format is None:
                data_format = u'id/tags/created/createdrel" ago"#created/vsize/diffsize'
            self.write_table(handle_wrapped, walking, all=all, data_format=data_format)
        elif output==u'treetable':
            if data_format is None:
                data_format = u'id/status#S/tags/created/createdrel" ago"#created/vsize/diffsize'
            self.write_treetable(handle_wrapped, walking, all=all, data_format=data_format, mode_ascii=mode_ascii)


