#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Cal:
    aa='cal'
    def calculate(self, value):
        self.value = eval(value)

class Talk:
    aa='talk'
    def talk(self):
        print("current value is %d" % self.value)

class test1(Cal, Talk):
    pass
