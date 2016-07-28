#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from .walker_item import WalkerItem

class WalkerBase(object): 
    def __init__(self):
        self._walker_items = {}
        self._roots = set()
        self._frozen_roots = None

    def get_walker_item(self, item):
        if isinstance(item, WalkerItem):
            item = item.item
        if item in self._walker_items:
            return self._walker_items[item]
        walker_item = WalkerItem(self, item)
        self._walker_items[item] = walker_item
        self._roots.add(walker_item)
        if self._frozen_roots is not None:
            self.froze_walker()

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

    def _remove_root(self, walker_item):
        if walker_item in self._roots:
            self._roots.remove(walker_item)
            if self._frozen_roots is not None:
                self.froze_walker()



