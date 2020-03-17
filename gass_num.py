#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""
猜数字100内，判断需要猜测几次
"""

def gassNum(top=100):
    target = 0
    count = 0 # 猜测次数

    while True:
        target = input("Please input number(1-100)")

        if not target.isdigit():
            print("Please input correct number(1-100)")
        else:
            target = int(target)
            break

    result = {
        'lower': 0,
        'upper': top,
        'middle': 0,
        'target': target,
        'count': 0,
    }

    gass(**result)


def gass(**args):
    middle = args['middle'] = int((args['lower'] + args['upper'])/2)
    target = args['target']
    args['count'] += 1
    print(args)

    if middle == target:
        return args
    else:
        if middle > target:
            args['upper'] = middle-1
        else:
            args['lower'] = middle+1
        gass(**args)

        

gassNum(100)

