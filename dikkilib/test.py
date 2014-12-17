#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import unittest
import sys
import os
from .dikki import Dikki
from .images import Images
from .image_walker import ImageWalker
from .image import Image
from . import time_mock
from . import tools
from .raw_docker_mock import RawDockerMock

class HandleMock(object):
    def __init__(self):
        self._content = u''

    def write(self, content):
        self._content += content.decode('utf-8')

class TestDikki(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self._stdout_backup = sys.stdout
        self._stdout = HandleMock()
        time_mock.current_time = 1418554800.

        tools.time = time_mock
        sys.stdout = self._stdout

        raw_docker = RawDockerMock()
        images = Images(Image, ImageWalker, raw_docker)
        self._dikki = Dikki(images)

    def test_stdout_mock(self):
        print "poide"
        print "praf"

        self.assertEqual(self._stdout._content, 'poide\npraf\n')

    def compare_result_files(self, command_line, filename):
        result = self._dikki.run(command_line)
        self.assertEqual(result, True)

        basefilename = os.path.join(os.path.dirname(__file__),'..','tests',filename)
        with open(basefilename+'.output','rb') as handle:
            expected_output = handle.read().decode('utf-8')

        with open(basefilename+'.actual.output','wb') as handle:
            handle.write(self._stdout._content.encode('utf-8'))

        self.assertEqual(self._stdout._content, expected_output)

    def test_tree(self):
        self.compare_result_files( ['tests.com', 'images', '-O', 'tree'], 'tree' )

    def test_tree_all(self):
        self.compare_result_files( ['tests.com', 'images', '--output=tree', '--all'], 'tree-all' )

    def test_tree_compact(self):
        self.compare_result_files( ['tests.com', 'images', '--output=tree', '--compact'], 'tree-compact' )

    def test_tree_compact_ascii(self):
        self.compare_result_files( ['tests.com', 'images', '--output=tree', '-cA'], 'tree-compact-ascii' )

    def test_graph(self):
        self.compare_result_files( ['tests.com', 'images', '--output=digraph'], 'graph' )

    def test_graph_all(self):
        self.compare_result_files( ['tests.com', 'images', '--output=digraph', '-a'], 'graph-all' )

    def test_graph_point(self):
        self.compare_result_files( ['tests.com', 'images', '--output=digraph', '--point'], 'graph-point' )

    def test_graph_point_all(self):
        self.compare_result_files( ['tests.com', 'images', '--output=digraph', '-ap'], 'graph-point-all' )

    def test_table(self):
        self.compare_result_files( ['tests.com', 'images', '--output=table'], 'table' )

    def test_treetable(self):
        self.compare_result_files( ['tests.com', 'images', '-O', 'treetable'], 'treetable' )

    def test_treetable_format(self):
        self.compare_result_files( ['', 'images', '-O', 'treetable', '-f', '"[ "createdrel" ]"#CREATED/tags< :: >#TAGS'], 'treetable-format' )

    def test_help(self):
        self.compare_result_files( ['dikki.py', 'help', '--help'], 'help-help' )

    def debug(self, name, value):
        self._stdout_backup.write('%s: [%r]\n' % (name, value))

    def tearDown(self):
        sys.stdout = self._stdout_backup
        tools.time = time_mock.backup_time

