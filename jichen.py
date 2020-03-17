#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Filter:
    def init(self):
        self.block = []

    def filter(self,data):
        return [ x for x in data if x not in self.block ]

class a1(Filter):
    def init(self):
        self.block = ['span']

tmpList = ['span', 'aa', 'span', 'bb']
