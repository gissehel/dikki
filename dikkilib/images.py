#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import docker
from itertools import chain
from .image_walker import ImageWalker
from .image import Image
from .tools import human_readable_bytes
from .tools import write_tree

class Images(object):
    def __main__(self) :
        self._by_id = {}
        self._by_tag = {}

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
        for walker_item, prefix in walking:
            image = walker_item.item
            children = [ walker_child.item for walker_child in walker_item.children ]
            for child in children:
                handle.write(' %s -> %s\n' % (image.name, child.name))
            if len(image.tags)>0:
                handle.write(' %s [label="%s",shape=box,fillcolor="paleturquoise",style="filled,rounded"];\n' % (image.name, '\\n'.join([image.sid] + sorted(image.tags))))
            elif as_point:
                handle.write(' %s [label="%s",shape="point"];\n' % (image.name, ''))
        handle.write('}\n')
        
    def classic_format_tree_line(self, handle, image):
        handle.write(image.sid)
        handle.write(' Virtual Size: ')
        handle.write(human_readable_bytes(image.virtual_size))
        if len(image.tags)>0:
            handle.write(' Tags: ' + ', '.join(image.tags))

    def compact_format_tree_line(self, handle, image):
        handle.write(image.sid)
        if len(image.tags)>0:
            handle.write('     ' + '  '.join(image.tags))

    def get_walking_object(self, tag='', all=False):
        ref_images = self.find_image(tag)
        walker = self._image_walker if all else self._important_image_walker

        if ref_images is None:
            walking = walker.walk()
        else:
            walking = chain.from_iterable(walker.get_walker_item(ref_image).walk() for ref_image in sorted(ref_images, key=lambda image:-image.created))

        return walking

    def load_images(self):
        d = docker.Client(base_url='unix://var/run/docker.sock', version='1.13', timeout=10)
        # self._root_image = Image()
        images = [ Image(raw_image) for raw_image in d.images(quiet=False, all=True) ] # + [ self._root_image ]

        self._by_id = {}
        self._by_tag = {}
        self._image_walker = ImageWalker()
        self._important_image_walker = ImageWalker()

        for image in images :
            self._by_id[image.lid] = image
            for tag in image.tags:
                self._by_tag[tag] = image

        for image in images :
            if image.parent_lid in self._by_id:
                image.set_parent(self._by_id[image.parent_lid])
                self._image_walker.set_parent(image, self._by_id[image.parent_lid])

        #for image in images :
        #    image.sort_children()

        self._image_walker.froze_walker()
        important_parents = {}
        for walker_item, prefix in self._image_walker.walk():
            image = walker_item.item
            if walker_item.parent is None:
                pass
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

    def write_result(self, handle, tag='', all=False, as_point=True, mode_tree=False, mode_compact=False, mode_ascii=False):
        self.load_images()
        walking = self.get_walking_object(tag, all=all)
        if mode_tree:
            if mode_compact:
                formatter = self.compact_format_tree_line
            else:
                formatter = self.classic_format_tree_line
            write_tree(handle, walking, formatter, mode_ascii)
        else:
            self.write_digraph(handle, walking, as_point=as_point)

