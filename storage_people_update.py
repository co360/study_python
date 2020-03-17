#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""
存储人名
"""

result = {}
labels = 'first','middle','last'

def init():
    result.setdefault(labels[0], {})
    result.setdefault(labels[1], {})
    result.setdefault(labels[2], {})

def lookup(data,label,first_name):
    return data.get(label, {}).setdefault(first_name, [])

def store(name):
    names = name.strip().split()
    if len(names) == 2:
        names.insert(1, '')
    elif not len(names):
        print("Please input names like 'ha li luya'")
        return False

    for label,key in zip(labels,names):
        people = lookup(result,label,key)
        if people:
            if name not in people:
                people.append(name)
        else:
            people.append(name)

def showPeople():
    print(result)

if __name__ == '__main__':
    init()
    store('wang hao')
    showPeople()
    store('wang hao')
    showPeople()
    store('tan mu xun')
    store('wang yu hao')
    showPeople()



