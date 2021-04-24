#!/usr/bin/env python3
# coding: utf-8

from .tools import write_table
from .tools import get_tree_prefix

class Attributable(object):
    def get_headers(self, attributes):
        result = []
        for attribut in attributes:
            if '#' in attribut:
                attribut = attribut.split('#',1)[1]
            subattributes, texts = [ attribut.split('"')[index::2] for index in range(2) ]
            result.append(' '.join(filter(len,subattributes)))
        return result

    def get_attributes(self, walker_item, attributes):
        result = []

        for attribut in attributes:
            if '#' in attribut:
                attribut = attribut.split('#',1)[0]
            attribut_value = ''
            has_value = False
            subattributes, texts = [ attribut.split('"')[index::2] for index in range(2) ]
            for index in range(len(subattributes)):
                subattribut = subattributes[index]
                arg = None
                if '<' in subattribut and subattribut.endswith('>'):
                    subattribut, arg = subattribut[:-1].split('<',1)
                if subattribut in self._attribut_getter:
                    if arg is None :
                        value = self._attribut_getter[subattribut](walker_item)
                    else:
                        value = self._attribut_getter[subattribut](walker_item, arg)
                    if len(value)>0:
                        has_value = True
                    attribut_value += value
                if index<len(texts):
                    attribut_value += texts[index]
            if has_value or all(len(subattribut)==0 for subattribut in subattributes):
                result.append(attribut_value)
            else:
                result.append('')
        return result

    def get_tree_attributes(self, walker_item, prefix, attributes, mode_ascii):
        iterator = iter(self.get_attributes(walker_item, attributes))
        try:
            first_attribut = next(iterator)
            yield get_tree_prefix(prefix, mode_ascii)+first_attribut
            for item in iterator:
                yield item
        except StopIteration:
            pass

    def write_table(self, handle, walking, all=False, data_format='id'):
        attributes = data_format.split('/')
        write_table(handle, (self.get_attributes(walker_item, attributes) for walker_item, prefix in walking if all or walker_item.item.is_important), self.get_headers(attributes), '=')

    def write_treetable(self, handle, walking, all=False, data_format='id', mode_ascii=False):
        attributes = data_format.split('/')
        write_table(handle, (self.get_tree_attributes(walker_item, prefix, attributes, mode_ascii) for walker_item, prefix in walking if all or walker_item.item.is_important), self.get_headers(attributes), '=')

