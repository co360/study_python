#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
