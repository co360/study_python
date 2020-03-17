#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""
斐波那契数列
"""

def fibs(num):
    result = [0,1]
    for num in range(num - 1):
        result.append(result[-2] + result[-1])
    return result

print(fibs(10))
print(fibs(20))
