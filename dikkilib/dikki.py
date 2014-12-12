#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import
import sys
from cltools import CLRunner
from supertools import superable
from .images import Images

@CLRunner.runnable()
@superable
class Dikki(object):
    '''Docker tool to query informations from images and containers'''
    def __init__(self):
        pass

    @CLRunner.command(params={
        'output': {'doc':'Output the images as [tree|digraph]', 'aliases': ['O'], 'need_value': True},
        'all': {'doc':'Display all nodes', 'aliases': ['a']},
        'compact': {'doc':'Display trees with compact pattern', 'aliases': ['c']},
        'ascii': {'doc':'Display trees with ascii chars', 'aliases': ['A']},
        'point': {'doc':'Display non-important nodes as point in graphs', 'aliases': ['p']},
        })
    def images(self, args, kwargs):
        """Get docker images"""
        # print (args, kwargs)
        outputs = ('tree','digraph')
        if 'output' not in kwargs:
            self.errorexit('You must provide an output for images. Correct values are : %s' % (', '.join(list(outputs)),))
        if kwargs['output'] not in outputs:
            self.errorexit('[%s] is invalid : output must be one of : %s' % (kwargs['output'], ', '.join(list(outputs))))
        if len(args) > 1:
            self.errorexit('Currently this tool only support one tag as argument.')
        tag = ''
        if len(args) > 0:
            tag = args[0]
        Images().write_result(sys.stdout, tag, all=('all' in kwargs), as_point=('point' in kwargs), mode_tree=(kwargs['output']=='tree'), mode_compact=('compact' in kwargs), mode_ascii=('ascii' in kwargs))


    @CLRunner.param(name='help',aliases=['h'])
    def help_param(self,**kwargs) :
        '''Get help on specific command'''
        self.help_on_command(**kwargs)

    @CLRunner.command()
    def help(self, args=[], kwargs={}) :
        """give help"""
        self.__super.help()

