#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
f(0) = 1，f(1) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数
"""

def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2*fn(n-1) + fn(n-2)

print(fn(10))

"""
f(20) = 1，f(21) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数
"""

def fn2(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    else:
        return fn2(n+2) - 2*fn(n+1)

print(fn2(10))

