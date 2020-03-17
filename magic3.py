#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Size:
    def __init__(self):
        self.width = 10
        self.height = 15

    def getSize(self):
        return self.width, self.height
    
    def setSize(self, width, height):
        self.width = width
        self.height = height

class Size2(Size):
    def __init__(self):
        super(Size2, self).__init__()
        self.size = property(self.getSize, self.setSize)
