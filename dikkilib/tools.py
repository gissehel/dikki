#!/usr/bin/env python
# coding: utf-8

import yaml
import sys
from math import log

def show(obj):
    print yaml.safe_dump(obj, default_flow_style=False)

def write_tree(handle, walking, item_formatter, mode_ascii=False):
    if mode_ascii:
        font = ' | `+-'
    else:
        font = (' ','│',' ','└','├','─')
    for walker_item, prefix in walking:
        for prefix_part in prefix[:-1]:
            if prefix_part :
                handle.write(font[0])
            else:
                handle.write(font[1])
            handle.write(font[2])
        for prefix_part in prefix[-1:]:
            if prefix_part :
                handle.write(font[3])
            else:
                handle.write(font[4])
            handle.write(font[5])
        item_formatter(handle, walker_item.item)
        handle.write('\n')

def human_readable_bytes(x):
    # hybrid of http://stackoverflow.com/a/10171475/2595465
    #      with http://stackoverflow.com/a/5414105/2595465
    if x == 0: return '0'
    magnitude = int(log(abs(x),10))
    if magnitude > 16:
        format_str = '%i P'
        denominator_mag = 15
    else:
        float_fmt = '%2.1f' if magnitude % 3 == 1 else '%1.2f'
        illion = (magnitude) // 3
        format_str = float_fmt + [' B', ' kB', ' MB', ' GB', ' TB', ' PB'][illion]
    return (format_str % (x * 1.0 / (1000 ** illion))).lstrip('0')

