#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

class Clanguage:
    name = 'C language'
    add = 'https://www.wmsj100.com'
    
    def say(self, cont):
        print(cont)

a = Clanguage()
print(a.name)
b = Clanguage()
print(b.name)
Clanguage.name = 'wmsj100'
print(a.name)
print(b.name)

