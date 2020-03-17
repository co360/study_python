#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def power1(m,n):
    result = 1
    for i in range(n):
        result *= m
    return result

def power2(m,n):
    if n == 0:
        return 1
    else:
        return m * power2(m,n-1)

print(power1(3,3))
print(power2(3,3))
