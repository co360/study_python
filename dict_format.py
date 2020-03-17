#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""

"""
temp = '''
<!doctype html>
<head>
    <title>%(title)s</title>
</head>
<body>
    <h1>%(title)s</h1>
    <p><span>%(text)s</span></p>
</body>'''

dict1 = {
    'title': 'wmsj100 blog',
    'text': 'this is a blog website!'
        }

print(temp % dict1)
