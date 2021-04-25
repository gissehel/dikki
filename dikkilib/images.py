#!/usr/bin/env python3
# coding: utf-8

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
            xtag = xtag + ':latest'
        if xtag in self._by_tag:
            return [ self._by_tag[xtag] ]
        ids = [xid for xid in self._by_id if xid.lower().startswith(tag)]
        if len(ids) == 0:
            raise Exception('No image found (%r)' % (tag,))
        else:
            return [ self._by_id[id] for id in ids ]

    def write_digraph(self, handle=None, walking=None, as_point=True):
        handle.write('digraph docker {\n')
        handle.write('  rankdir="LR";\n')
        for walker_item, prefix in walking:
            image = walker_item.item
            children = [ walker_child.item for walker_child in walker_item.children ]
            for child in children:
                handle.write(' "%s" -> "%s"\n' % (image.sid, child.sid))
            if len(image.tags)>0:
                handle.write(' %s [label="%s",shape=box,fillcolor="paleturquoise",style="filled,rounded"];\n' % (image.name, '\\n'.join([image.sid] + sorted(image.tags))))
            elif as_point:
                handle.write(' %s [label="%s",shape="point"];\n' % (image.name, ''))
        handle.write('}\n')
        
    def classic_format_tree_line(self, handle, walker_item):
        handle.write(walker_item.item.sid)
        handle.write(' Virtual Size: ')
        handle.write(human_readable_bytes(walker_item.item.virtual_size))
        if len(walker_item.item.tags)>0:
            handle.write(' Tags: ' + ', '.join(walker_item.item.tags))

    def compact_format_tree_line(self, handle, walker_item):
        handle.write(walker_item.item.sid)
        if len(walker_item.item.tags)>0:
            handle.write('     ' + '  '.join(walker_item.item.tags))

    def get_tree_formatter(self, generic_format):
        def tree_formatter(handle, walker_item):
            for count, value in enumerate(self.get_attributes(walker_item, generic_format.split('/'))):
                if count > 0 and len(value) > 0:
                    handle.write(' ')
                handle.write(value)
        return tree_formatter

    def get_walking_object(self, tag='', all=False):
        ref_images = self.find_image(tag)
        walker = self._image_walker if all else self._important_image_walker

        if ref_images is None:
            walking = walker.walk()
        else:
            walking = chain.from_iterable(walker.get_walker_item(ref_image).walk() for ref_image in sorted(ref_images, key=lambda image:-image.get_created()))

        return walking

    def load_images(self, root_as_important=False):
        images = [ self._Image(raw_image=raw_image, image_info=self._raw_docker.get_image_info(raw_image['Id'])) for raw_image in self._raw_docker.get_images() ]

        self._by_id = {}
        self._by_tag = {}
        self._by_tid = {}
        self._image_walker = self._ImageWalker()

        for image in images :
            self._by_id[image.lid] = image
            if image.tid is not None:
                if image.tid not in self._by_tid:
                    self._by_tid[image.tid] = []
                self._by_tid[image.tid].append(image)
            for tag in image.tags:
                self._by_tag[tag] = image

        for image in images :
            if image.parent_lid in self._by_id:
                image.set_parent(self._by_id[image.parent_lid])
                self._image_walker.set_parent(image, self._by_id[image.parent_lid])
            else:
                self._image_walker.get_walker_item(image)

        for image_walker in list(self._image_walker._roots):
            current_image = image_walker.item
            continuation = True
            while continuation and current_image.parent_tid is not None:
                if current_image.parent_tid in self._by_tid:
                    parent_image = self._by_tid[current_image.parent_tid][0]
                else:
                    parent_image = self._Image(tids=current_image.tids[:-1])
                    if current_image.parent_tid not in self._by_tid:
                        self._by_tid[current_image.parent_tid] = []
                    self._by_tid[current_image.parent_tid].append(parent_image)

                if self._image_walker.get_walker_item(current_image).parent is None:
                    current_image.set_parent(parent_image)
                    self._image_walker.set_parent(current_image, parent_image)
                    current_image = parent_image
                else:
                    continuation = False


        self._image_walker.froze_walker()

        important_parents = {}
        self._important_image_walker = self._ImageWalker()
        for walker_item, prefix in self._image_walker.walk():
            image = walker_item.item
            if walker_item.parent is None:
                if walker_item.is_important(root_as_important=root_as_important):
                    if root_as_important:
                        self._important_image_walker.get_walker_item(image)
            else:
                parent = walker_item.parent.item
                if walker_item.parent.is_important(root_as_important=root_as_important):
                    if walker_item.is_important(root_as_important=root_as_important):
                        self._important_image_walker.set_parent(image, parent)
                    important_parents[image] = parent
                else:
                    if parent in important_parents:
                        if walker_item.is_important(root_as_important=root_as_important):
                            self._important_image_walker.set_parent(image, important_parents[parent])
                        important_parents[image] = important_parents[parent]
                    else:
                        if walker_item.is_important(root_as_important=root_as_important):
                            self._important_image_walker.get_walker_item(image)
        self._important_image_walker.froze_walker()

    def load_status(self):
        containers = [ self._Container(raw_container, self._raw_docker.get_container_info(raw_container['Id'])) for raw_container in self._raw_docker.get_containers() ]
        for container in containers:
            if container.imagelid in self._by_id:
                if container.running:
                    self._by_id[container.imagelid].set_running()
                else:
                    self._by_id[container.imagelid].set_stopped()
                loop_image_walker = self._image_walker.get_walker_item(self._by_id[container.imagelid])
                while loop_image_walker is not None:
                    if loop_image_walker.item is not None:
                        loop_image_walker.item.set_child_stop_or_running()
                    loop_image_walker = loop_image_walker.parent

    _attribut_getter = {
        'id': (lambda walker_item: walker_item.item.sid),
        'longid': (lambda walker_item: walker_item.item.lid),
        'title': (lambda walker_item: walker_item.item.title if walker_item.item.title is not None else ''),
        'version': (lambda walker_item: walker_item.item.version if walker_item.item.version is not None else ''),
        'tags': (lambda walker_item,sep=' ': sep.join(sorted(walker_item.item.tags))),
        'vsize': (lambda walker_item: human_readable_bytes(walker_item.recursive_get('virtual_size'))),
        'diffsize': (lambda walker_item: (human_readable_bytes(walker_item.recursive_get('virtual_size')-(walker_item.parent.recursive_get('virtual_size') if walker_item.parent is not None else 0) if walker_item.parent is not None and walker_item.parent.recursive_get('virtual_size') is not None else walker_item.recursive_get('virtual_size')))),
        'size': (lambda walker_item: human_readable_bytes(walker_item.item.size)),
        'parentid': (lambda walker_item: (walker_item.parent.item.sid if walker_item.parent is not None else '')),
        'created': (lambda walker_item: format_time(walker_item.item.get_created())),
        'createdrel': (lambda walker_item: format_time_rel(walker_item.item.get_created())),
        'status': (lambda walker_item: walker_item.item.get_run_status())
        }

    def write_result(self, handle, tag='', all=False, root_as_important=False, as_point=True, output=None, mode_compact=False, mode_ascii=False, data_format=None):
        self.load_images(root_as_important=root_as_important)
        self.load_status()
        handle_wrapped = wrap_handle(handle,'utf-8')
        walking = self.get_walking_object(tag, all=all)
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
                data_format = 'id/tags/title/version/created/createdrel" ago"#created/vsize/diffsize'
            self.write_table(handle_wrapped, walking, all=all, data_format=data_format)
        elif output=='treetable':
            if data_format is None:
                data_format = 'id/status#S/tags/title/version/created/createdrel" ago"#created/vsize/diffsize'
            self.write_treetable(handle_wrapped, walking, all=all, data_format=data_format, mode_ascii=mode_ascii)


