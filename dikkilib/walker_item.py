#!/usr/bin/env python3
# coding: utf-8

class WalkerItem(object):
    def __init__(self, walker, item):
        self._walker = walker
        self.item = item
        self.parent = None
        self.children = []
        self._attr_cache = {}

    def is_root(self):
        return self.parent is None

    def set_parent(self, parent):
        walker_parent = self._walker.get_walker_item(parent)
        self.parent = walker_parent
        walker_parent.children.append(self)
        self._walker._remove_root(self)

    def walk(self):
        yield (self, [])
        if len(self.children)>0 :
            for subitem in self.children[:-1]:
                for item, prefix in subitem.walk():
                    yield (item, [False]+prefix)
            for item, prefix in self.children[-1].walk():
                yield (item, [True]+prefix)

    def is_important(self, root_as_important=False):
        return self.item.is_important() or len(self.children)!=1 or (root_as_important and (self.parent is None))

    def recursive_get(self, prop):
        if prop not in self._attr_cache:
            value = getattr(self.item, prop)
            if value is None and self.parent is not None:
                value = self.parent.recursive_get(prop)
            self._attr_cache[prop] = value
        return self._attr_cache[prop]

