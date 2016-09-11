#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
from .walker_base import WalkerBase

class ImageWalker(WalkerBase):
    def sort(self, list):
        list.sort(key=lambda walker_item:-walker_item.item.get_created())


