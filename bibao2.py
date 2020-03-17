#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
计算n次幂
"""

def fn(n):
    def fn2(m):
        return m**n
    return fn2

pinf = fn(2)
lif = fn(3)

print(pinf(5))
print(lif(5))
