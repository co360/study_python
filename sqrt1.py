#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""
找出100内最大的平方数
"""
from math import sqrt

for num in range(99,81,-1):
    val = sqrt(num)
    if val == int(val):
        print(num)
        break
else:
    print("nothind")
