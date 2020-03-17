#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def hello(**args):
    print(args['name'], args['age'])

data = { 'name': 'wmsj100', 'age': 32}

hello(**data)

def hello2(args):
    print(args['name'], args['age'])

hello2(data)
