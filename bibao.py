#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
def fn1(num):
    def fn2(num2):
        return num*num2
    return fn2

print(fn1(5))
print(fn1(5)(3))

