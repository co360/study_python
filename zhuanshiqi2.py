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

def logged(level):
    if not callable(level):
        def _deco(func):
            @functools.wraps(func)
            def _deco(*args, **kwargs):
                print("decorate has argument")
                print('arguments is {}'.format(level))
                return func(*args, **kwargs)
            return _deco
        return _deco
    else:
        @functools.wraps(level)
        def _deco(*args, **kwargs):
            print("decorate doesn't has argemunt")
            level(*args, **kwargs)
        return _deco

def logging(level):
    def _deco(func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if level == 'warn':
                print('{} is warning logging running, please lookup'.format(func.__name__))
            return func(*args, **kwargs)
        return _deco
    return _deco

def use_logging(func):
    @functools.wraps(func)
    def _deco(*args, **kwargs):
        print("{} is use_logging running".format(func.__name__))
        print("all function complete")
        return func(*args, **kwargs)
    return _deco

#@logging('pass')
#@use_logging
def bar(a,b):
    print('i am bar, result is {}'.format(a*b))

#bar(2,5)

class Log_class:
    def __init__(self, args='warn'):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if self.args == 'warn':
                self.notify(func)
            return func(*args, **kwargs)
        return _deco

    def notify(self, func):
        print('{} is running'.format(func.__name__))

class email_log(Log_class):
    def __init__(self, email='wmsj100@hotmail.com', *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)

    def notify(self, func):
        print('Please send email to {}'.format(self.email))
        print('{} is running'.format(func.__name__))


#@Log_class(args='warning')
@email_log(args='warning')
#@logged('wmsj param')
#@logged
#@logging('warn')
#@use_logging
def bar2(a,b,c,d):
    print('i am bar2, data is {}'.format(a+b+c+d))
    print(bar2.__name__)

bar2(4,3,5,6)
