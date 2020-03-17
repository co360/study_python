#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

def double(list):
    for index in range(len(list)):
        list[index] = list[index]*2
    return list

def han_shu_double(list):
    result = []
    for val in list:
        result.append(val*2)
    return result

print(double([2,4,3,6]))
print(han_shu_double([2,4,3,6]))
