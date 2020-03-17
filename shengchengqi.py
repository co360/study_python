#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
class Flatten:
    def __init__(self):
        pass

    def flatten(self, list):
        for sublist in list:
            for element in sublist:
                yield element


#list1 = [[1,2],[3,4],[5]]
#
#def flatten(list):
#    for sublist in list:
#        for element in sublist:
#            yield element
#
#
#for num in flatten(list1):
#    print(num)

class Digui:
    def __init__(self):
        pass

    def flatten(self, listVal):
        try:
            for sublist in listVal:
                for element in self.flatten(sublist):
                    yield element
        except TypeError:
            yield listVal

class Digui1:
    def __init__(self):
        pass

    def flatten(self, listVal):
        try:
            try:
                listVal + ''
            except TypeError: pass
            else: raise TypeError

            for sublist in listVal:
                for element in self.flatten(sublist):
                    yield element

        except TypeError:
            yield listVal
