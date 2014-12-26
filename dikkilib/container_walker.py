#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from .walker_base import WalkerBase


class ContainerWalkerItem(object):
    def __init__(self,item):
        self.item = item

class ContainerWalker(object):
    def __init__(self, items):
        self._walker_items = [ ContainerWalkerItem(item) for item in items ]

    def walk(self):
        for walker_item in self._walker_items:
            yield walker_item, []
        


