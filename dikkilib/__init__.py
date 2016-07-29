#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import sys
from .dikki import Dikki
from .image import Image
from .images import Images
from .image_walker import ImageWalker
from .container import Container
from .containers import Containers
from .container_walker import ContainerWalker
from .raw_docker import RawDocker

def main() :
    raw_docker = RawDocker()
    images = Images(Image, ImageWalker, Container, raw_docker)
    containers = Containers(Container, ContainerWalker, raw_docker)
    dikki = Dikki(images, containers, raw_docker)
    if not(dikki.run( sys.argv )) :
        sys.exit(1)


