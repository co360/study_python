#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""
from redis import Redis

myredis = Redis(host='127.0.0.1',port=6379)

myredis.set('age', '34')
print(myredis.get('age'))
myredis.delete('age')
myredis.set('view', 1)
print(myredis.get('view'))
myredis.incr('view')
print(myredis.get('view'))
myredis.decr('view')
print(myredis.get('view'))
