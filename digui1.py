#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def jiechen(n):
    if n <= 1:
        return 1
    else:
        return n*jiechen(n-1)

print(jiechen(5))

def fn(n):
    result = 1
    for num in range(n):
        result *= n
        n -= 1
    return result

print(fn(5))
