#!/usr/bin/env python
# coding: utf-8

import docker
import yaml
import sys
from math import log
from itertools import chain

def show(obj):
    print yaml.safe_dump(obj, default_flow_style=False)

class WalkerItem(object):
    def __init__(self, walker, item):
        self._walker = walker
        self.item = item
        self.parent = None
        self.children = []

    def is_root(self):
        return self.parent is None

    def set_parent(self, parent):
        walker_parent = self._walker.get_walker_item(parent)
        self.parent = walker_parent
        walker_parent.children.append(self)
        if self in self._walker._roots:
            self._walker._roots.remove(self)
            if self._walker._frozen_roots is not None:
                self._walker._frozen_roots = list(self._walker._roots)
                self.sort(self._walker._frozen_roots)

    def walk(self):
        yield (self, [])
        if len(self.children)>0 :
            for subitem in self.children[:-1]:
                for item, prefix in subitem.walk():
                    yield (item, [False]+prefix)
            for item, prefix in self.children[-1].walk():
                yield (item, [True]+prefix)

class Walker(object): 
    def __init__(self):
        self._walker_items = {}
        self._roots = set()
        self._frozen_roots = None

    def get_walker_item(self, item):
        if isinstance(item, WalkerItem):
            return item
        if item in self._walker_items:
            return self._walker_items[item]
        walker_item = WalkerItem(self, item)
        self._walker_items[item] = walker_item
        self._roots.add(walker_item)
        if self._frozen_roots is not None:
            self._frozen_roots = list(self._roots)
            self.sort(self._frozen_roots)

        return walker_item

    def froze_walker(self):
        self._frozen_roots = list(self._roots)
        self.sort(self._frozen_roots)

        for walker_item in self._walker_items.values():
            self.sort(walker_item.children)

    def sort(self, list):
        list.sort()

    def set_parent(self, item, parent_item):
        walker_item = self.get_walker_item(item)
        walker_item.set_parent(parent_item)

    def walk(self):
        for walk_item in self._frozen_roots:
            for item, prefix in walk_item.walk():
                yield (item, prefix)

class ImageWalker(Walker):
    def sort(self, list):
        list.sort(key=lambda walker_item:-walker_item.item.created)

def write_tree(handle, walking, item_formatter, mode_ascii=False):
    if mode_ascii:
        font = ' | `+-'
    else:
        font = (' ','│',' ','└','├','─')
    for walker_item, prefix in walking:
        for prefix_part in prefix[:-1]:
            if prefix_part :
                handle.write(font[0])
            else:
                handle.write(font[1])
            handle.write(font[2])
        for prefix_part in prefix[-1:]:
            if prefix_part :
                handle.write(font[3])
            else:
                handle.write(font[4])
            handle.write(font[5])
        item_formatter(handle, walker_item.item)
        handle.write('\n')

def human_readable_bytes(x):
    # hybrid of http://stackoverflow.com/a/10171475/2595465
    #      with http://stackoverflow.com/a/5414105/2595465
    if x == 0: return '0'
    magnitude = int(log(abs(x),10))
    if magnitude > 16:
        format_str = '%i P'
        denominator_mag = 15
    else:
        float_fmt = '%2.1f' if magnitude % 3 == 1 else '%1.2f'
        illion = (magnitude) // 3
        format_str = float_fmt + [' B', ' kB', ' MB', ' GB', ' TB', ' PB'][illion]
    return (format_str % (x * 1.0 / (1000 ** illion))).lstrip('0')

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
            self.is_root = False
        self.children = []
        self.parent = None

    #def sort_children(self):
    #    self.children.sort(key=lambda image:-image.created)

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def is_important(self):
        return len(self.tags)>0 or len(self.children)!=1

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

def main() :
    tag = ''
    all = False
    as_point = False
    mode_tree = False
    mode_compact = False
    mode_ascii = False
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            for letter in arg[1:]:
                if letter == 'a':
                    all = True
                elif letter == 'p':
                    as_point = True
                elif letter == 't':
                    mode_tree = True
                elif letter == 'c':
                    mode_compact = True
                elif letter == 'A':
                    mode_ascii = True
        else:
            tag = arg
    Images().write_result(sys.stdout, tag, all=all, as_point=as_point, mode_tree=mode_tree, mode_compact=mode_compact, mode_ascii=mode_ascii)

main()

