#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import sys
from .dikki import Dikki

def main() :
    dikki = Dikki()
    if not(dikki.run( sys.argv )) :
        sys.exit(1)


