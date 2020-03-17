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
    def __init__(self, name):
        self.name = name

    def say(self):
        print("I am people {}".format(self.name))

class Animal:
    def __init__(self, food):
        self.food = food

    def eat(self):
        print("I eat food {}".format(self.food))

class Anys(People, Animal):
    def __init__(self, name, food):
        super().__init__(name)
        Animal.__init__(self, food)



