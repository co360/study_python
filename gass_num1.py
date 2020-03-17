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
import math
def gassNum(top=100):
    target = 0
    tmp = 0 # 临时的值
    count = 0 # 猜测次数

    while True:
        target = input("Please input number(1-100)")

        if not target.isdigit():
            print("Please input correct number(1-100)")
        else:
            target = int(target)
            break

    result = {
        'tmp': math.floor(top/2),
        'top': top,
        'target': target,
        'count': 1,
        'gassList': [math.floor(top/2)]
            }

    gass(**result)

def gass(**args):
    print(args)
    tmp=args['tmp']
    target = args['target']
    top = args['top']

    if args['tmp'] == args['target']:
        print("complete")
        return args
    else:
        args['count'] += 1
        if tmp > target:
            tmp = math.floor((tmp - 1)/2)
        else:
            tmp = math.floor((tmp + top)/2)
        args['tmp'] = tmp
        judgeExist(**args)
        gass(**args)
        
def judgeExist(**args):
    tmp = args['tmp']
    gassList = args['gassList']
    top = args['top']

    if tmp in gassList:
        for index in range(tmp,top):
            if index not in gassList:
                tmp = index
                args['tmp'] = tmp
    else:
        args['gassList'].append(tmp)

gassNum()

