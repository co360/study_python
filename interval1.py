#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def interval(start,stop=None, step=1):
    if stop is None:
        start,stop = 0, start
    result = []

    index = start;
    while index < stop:
        result.append(index)
        index += step
    return result

print(interval(5))
print(interval(5, 10))
print(interval(1, 10, 3))
