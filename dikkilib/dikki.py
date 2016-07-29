#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import sys
from cltools import CLRunner
from supertools import superable


@CLRunner.runnable()
@superable
class Dikki(object):
    '''Docker tool to query informations from images and containers'''
    def __init__(self, images, containers, raw_docker):
        self._images = images
        self._containers = containers
        self._raw_docker = raw_docker

    @CLRunner.command(params={
        'output': {'doc':'Output the images as [tree|digraph|table|treetable]', 'aliases': ['O'], 'need_value': True},
        'all': {'doc':'Display all nodes', 'aliases': ['a']},
        'compact': {'doc':'Display trees with compact pattern', 'aliases': ['c']},
        'ascii': {'doc':'Display trees with ascii chars', 'aliases': ['A']},
        'point': {'doc':'Display non-important nodes as point in graphs', 'aliases': ['p']},
        'format': {'doc':'Format for table, tree and treetable', 'aliases': ['f'], 'need_value': True},
        })
    def images(self, args, kwargs):
        """Get docker images"""
        # print (args, kwargs)
        outputs = (u'tree',u'digraph',u'table',u'treetable')
        if 'output' not in kwargs:
            output = u'treetable'
            # self.errorexit(u'You must provide an output for images. Correct values are : %s' % (u', '.join(list(outputs)),))
        else:
            output = kwargs['output']
        if output not in outputs:
            self.errorexit(u'[%s] is invalid : output must be one of : %s' % (output, u', '.join(list(outputs))))
        if len(args) > 1:
            self.errorexit(u'Currently this tool only support one tag as argument.')
        tag = ''
        if len(args) > 0:
            tag = args[0]
        self._images.write_result(sys.stdout, tag, all=('all' in kwargs), as_point=('point' in kwargs), output=output, mode_compact=('compact' in kwargs), mode_ascii=('ascii' in kwargs), data_format=(kwargs['format'] if 'format' in kwargs else None))

    @CLRunner.command(params={
        'output': {'doc':'Output the images as [table]', 'aliases': ['O'], 'need_value': True},
        'all': {'doc':'Display all containers', 'aliases': ['a']},
        'format': {'doc':'Format for table', 'aliases': ['f'], 'need_value': True},
        })
    def containers(self, args, kwargs):
        """Get docker containers"""
        # print (args, kwargs)
        outputs = (u'table',)
        if 'output' not in kwargs:
            output = 'table'
            # self.errorexit(u'You must provide an output for images. Correct values are : %s' % (u', '.join(list(outputs)),))
        else:
            output = kwargs['output']
        if output not in outputs:
            self.errorexit(u'[%s] is invalid : output must be one of : %s' % (output, u', '.join(list(outputs))))
        if len(args) > 0:
            self.errorexit(u'Currently this tool doesn\'t support container name.')
        self._containers.write_result(sys.stdout, all=('all' in kwargs), output=output, mode_ascii=('ascii' in kwargs), data_format=(kwargs['format'] if 'format' in kwargs else None))

    @CLRunner.param(name='help',aliases=['h'])
    def help_param(self,**kwargs) :
        '''Get help on specific command'''
        self.help_on_command(**kwargs)

    @CLRunner.param(name='debug',aliases=['D'])
    def debug_docker(self, **kwargs):
        '''Log all docker communications to files'''
        self._raw_docker.set_debug(True)

    @CLRunner.command()
    def help(self, args=[], kwargs={}) :
        """Give help"""
        self.__super.help()

