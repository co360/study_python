#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a,self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self

a=Fibs()

for i in a:
    if i<10:
        print(i)
    else:
        break
