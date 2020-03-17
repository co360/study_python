#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def conflict(state, nextX):
    nextY = len(state) # 获取下一个值的行高度
    
    for h in range(nextY):
        print(abs(nextX - state[h]), '====', nextY-h)
        if abs(nextX - state[h]) in (0, nextY - h):
        #if nextX == state[h] or abs(nextX - state[h]) == state[h] - h:
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        #print("pos is %d" % pos)
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

print(list(queens(4)))
