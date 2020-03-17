#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""

"""
people = {
    'bob': {
            'phone': '2341',
            'addr': 'usa'
        },
    'tom': {
            'phone': '4444',
            'addr': 'qiaotou'
        }
}

label = {
    'p': 'phone',
    'a': 'addr'
}

user=input('Please input name: ')

if user in people:
    type = input("Please input phone(p) or addr(a)")
    user = user.strip().lower()
    type = type.strip().lower()
    
    if type in label:
        key = label[type]
        value = people[user][key]
        print("%s %s is %s" % (user, key, value))
    else:
        print("please input p or a")
else:
    print("Please input collect name")

