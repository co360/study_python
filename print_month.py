#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""
打印月份
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
ending = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st']
year = int(input('please input year: '))
month = int(input('Please input month(1-12): '))
day = int(input('Please input day(1-31): '))

print('%s %s.%d' %(months[month-1], str(day) + ending[day-1], year))
