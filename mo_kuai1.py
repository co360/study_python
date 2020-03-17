#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
Clang is a module for name, age
only jiekou for info get_name
pelase ues it
"""

class Clang:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __get_info(self):
        return (self.__name, self.__age)

    def __set_info(self, args):
        self.__name, self.__age = args

    def __del_info(self):
        self.__name = 'xxx'
        self.__age = 0

    def get_name(self):
        print('name is ',__name__)

    info = property(__get_info, __set_info, __del_info)

if __name__ == '__main__':
    test = Clang('wmsj100', 32)
    print(test.info)
    print('name is ',__name__)
