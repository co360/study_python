#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

class People:
    def say(self):
        print('I can say')

class Animal:
    def call(self):
        print("I can call")

class dog(People, Animal):
    def run(self):
        print('I can run')
