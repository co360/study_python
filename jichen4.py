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
    def __init__(self):
        print("A", end=' ')
    super().__init__()

class B:
    def __init__(self):
        print("B", end=' ')

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C", end=' ')

d = C()
