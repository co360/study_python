#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
举一个二分搜索的例子。给定一个非递减整数数组，和一个 target 值，要求你找到数组中最小的一个数 x，满足 x*x > target，如果不存在，则返回 -1。
"""

def fn(array, target):
    l,r = 0, len(array) - 1
    ret = -1

    while l <= r:
        m = (l + r)//2
        if array[m] * array[m] > target:
            ret = m
            r = m -1
        else:
            l = m + 1
    if ret == -1:
        return -1
    else:
        return array[ret]

print(fn(list(range(10)), 58))
print(fn(list(range(8)), 28))

def com(num, target):
    return num * num > target

def binary_search(array, target):
    l, r = 0, len(array) - 1
    ret = -1

    while l <= r:
        m = (l + r)//2
        if com(array[m], target):
            r = m -1
            ret = m
        else:
            l = m + 1
    return ret 

def solve(array, target):
    ret = binary_search(array, target)
    return ret if ret == -1 else array[ret]
print(solve(list(range(10)), 58))
print(solve(list(range(8)), 28))
