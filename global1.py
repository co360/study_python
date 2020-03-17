#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
a=3

def ha():
    global a
    a = a + 1
    print(a)

ha()
print(a)

def hb():
    b = a + 1
    print('b is %d' % b)

hb()

if True:
    b=3
    print(a,b)
print(a,b)
