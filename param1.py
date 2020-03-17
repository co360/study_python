#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""
函数的关键字参数和位置参数
"""

def hello(name,age):
    print("name is %s, age is %d" % (name, age))

def hello1(name='wmsj100', age=32):
    print("name is %s, age is %d" % (name, age))

if __name__ == '__main__':
    hello('wanghao', 32)
    hello1()
    hello1('wanghao')
    hello1('wanghao', 34)
    hello1(age=43, name='wanghao')
    hello1('wanghao', age=56)
