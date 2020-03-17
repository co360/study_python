#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
偏函数练习
"""
from functools import partial

def my_add(m,n):
    return m+n

my_add_5 = partial(my_add, m=5)

print(my_add_5(n=8)) # 必须使用关键字传参
print(my_add(5,8))

def class_info(level, count):
    return '{} level has student\'s count is {}'.format(level, count)

class_two_info = partial(class_info, level='two')

print(class_two_info(count=20))
print(class_info('two', 20))
