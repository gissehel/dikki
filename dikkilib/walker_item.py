#!/usr/bin/env python
# coding: utf-8

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

