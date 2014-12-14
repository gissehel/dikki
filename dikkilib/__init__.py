#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import sys
from .dikki import Dikki
from .images import Images
from .image_walker import ImageWalker
from .image import Image
from .raw_docker import RawDocker

def main() :
    raw_docker = RawDocker()
    images = Images(Image, ImageWalker, raw_docker)
    dikki = Dikki(images)
    if not(dikki.run( sys.argv )) :
        sys.exit(1)


