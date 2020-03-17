#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

class Area:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @area.deleter
    def area(self):
        self.__area = 'xxx'

a = Area(100)
print(a.area)
a.area = 200
print(a.area)
del a.area
print(a.area)
