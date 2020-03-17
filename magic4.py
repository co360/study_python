#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Size(list):
    def __init__(self, *args):
        super(Size, self).__init__(*args)
        self.width = 10
        self.height = 15

    def getSize(self):
        return self.width, self.height

    def setSize(self, size):
        self.width = size[0]
        self.height = size[1]

    size = property(getSize, setSize)
