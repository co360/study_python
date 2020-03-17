#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
__metaclass__=type

class Person:
    __name=""
    count = 1

    def init(self):
        Person.count += 1

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def greet(self):
        print('Hello,world! I\'m %s' % self.__name)


