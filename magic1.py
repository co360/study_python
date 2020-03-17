#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
class Type1:
    def __init__(self, value=123):
        self.value = value
    def show(self):
        return self.value
    def setValue(self, value):
        self.value = value

class Type2(Type1):
    def __init__(self, name='Type2'):
        super(Type2, self).__init__()
        self.name = name
    def sing(self):
        return self.name

