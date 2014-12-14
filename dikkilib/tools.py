#!/usr/bin/env python
# coding: utf-8

import yaml
import sys
import time
from math import log

def show(obj):
    print yaml.safe_dump(obj, default_flow_style=False)

def write_tree(handle, walking, formatter, mode_ascii=False):
    if mode_ascii:
        font = (' ','|',' ','`','+','-')
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
        formatter(handle, walker_item)
        handle.write('\n')

def _update_line(lines, lens, line):
    line_str = tuple(map(str,line))
    lines.append(line_str)
    line_len = map(len,line_str)
    if len(lens) < len(line_len):
        lens += ([0]*(len(line_len)-len(lens)))
    for index in xrange(min(len(lens),len(line_str))):
        lens[index] = max(lens[index], len(line_str[index]))
    return lens

def write_table(handle, enumerable, header=None, sep=None):
    lines = []
    lens = []
    if header is not None:
        lens = map(len,header)
        lens = _update_line(lines, lens, header)
    for line in enumerable:
        lens = _update_line(lines, lens, line)
    for index, line_str in enumerate(lines):
        z = '  '.join(map(lambda l:"%%-%ds" % (l,), lens[:len(line_str)]))
        handle.write(z % line_str)
        handle.write('\n')
        if index==0 and header is not None and sep is not None:
            handle.write(z % tuple(map(lambda l:sep[:1]*l,lens)))
            handle.write('\n')

def format_time(value):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(value))

def format_time_rel(value):
    diff = time.time()-value
    if diff<0:
        return "future"
    if diff <= 1:
        return "1 second"
    if diff < 60:
        return "%s seconds" % (int(diff),)
    diff = int(diff/60.)
    if diff == 1:
        return "1 minute"
    if diff < 60:
        return "%s minute" % (diff,)
    diff = int(diff/60.)
    if diff == 1:
        return "1 hour"
    if diff < 24:
        return "%s hours" % (diff,)
    diff = int(diff/24.)
    if diff == 1:
        return "1 day"
    if diff <= 365:
        return "%s days" % (diff,)
    diff = int(diff/365.25)
    if diff == 1:
        return "1 year"
    return "%s years" % (diff,)

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


