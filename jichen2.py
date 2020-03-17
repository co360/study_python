#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

class A:
    def method(self):
        print("CommnoA")

class B(A):
    pass

class C(A):
    def method(self):
        print("CommonC")

class D(B,C):
    pass

print(D().method())
