#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('{} {}().'.format(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('executes')
def now():
    print('2013-12-25')

now()
print(now.__name__)
