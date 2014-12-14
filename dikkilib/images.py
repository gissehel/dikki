#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from itertools import chain
from .tools import human_readable_bytes
from .tools import write_tree
from .tools import write_table
from .tools import format_time
from .tools import format_time_rel

class Images(object):
    def __init__(self, image_class, image_walker_class, raw_docker) :
        self._by_id = {}
        self._by_tag = {}
        self._Image = image_class
        self._ImageWalker = image_walker_class
        self._raw_docker = raw_docker

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
        }

    def get_headers(self, attributes):
        result = []
        for attribut in attributes:
            if '#' in attribut:
                attribut = attribut.split('#',1)[1]
            subattributes, texts = [ attribut.split('"')[index::2] for index in xrange(2) ]
            result.append(' '.join(filter(len,subattributes)))
        return result

    def get_attributes(self, walker_item, attributes):
        result = []

        for attribut in attributes:
            if '#' in attribut:
                attribut = attribut.split('#',1)[0]
            attribut_value = ''
            has_value = False
            subattributes, texts = [ attribut.split('"')[index::2] for index in xrange(2) ]
            for index in xrange(len(subattributes)):
                subattribut = subattributes[index]
                arg = None
                if '<' in subattribut and subattribut.endswith('>'):
                    subattribut, arg = subattribut[:-1].split('<',1)
                if subattribut in self._attribut_getter:
                    if arg is None :
                        value = self._attribut_getter[subattribut](walker_item)
                    else:
                        value = self._attribut_getter[subattribut](walker_item, arg)
                    if len(value)>0:
                        has_value = True
                    attribut_value += value
                if index<len(texts):
                    attribut_value += texts[index]
            if has_value or all(len(subattribut)==0 for subattribut in subattributes):
                result.append(attribut_value)
            else:
                result.append('')
        return result

    def write_table(self, handle, walking, all=False, data_format='id'):
        attributes = data_format.split('/')
        write_table(handle, (self.get_attributes(walker_item, attributes) for walker_item, prefix in walking if all or len(walker_item.item.tags)>0), self.get_headers(attributes), '=')

    def write_result(self, handle, tag='', all=False, as_point=True, output=None, mode_compact=False, mode_ascii=False, data_format=None):
        self.load_images()
        walking = self.get_walking_object(tag, all=all)
        if output=='tree':
            if data_format is None:
                if mode_compact:
                    data_format = 'id/" [ "tags" ]"'
                else:
                    data_format = 'id/"Virtual Size: "vsize/"Tags: "tags<, >'
            formatter = self.get_tree_formatter(data_format)
            write_tree(handle, walking, formatter, mode_ascii)
        elif output=='digraph':
            self.write_digraph(handle, walking, as_point=as_point)
        elif output=='table':
            if data_format is None:
                data_format = 'id/tags/created/createdrel" ago"#created/vsize/diffsize'
            self.write_table(handle, walking, all=all, data_format=data_format)


