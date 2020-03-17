#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.

"""

"""
import math

screen=100
input_val = input("Please input value: ")
input_len = len(input_val)
box_width = input_len + 6
left = math.floor((screen - input_len)/2)
print(' '*left + "+" + '-' *(box_width - 2) + '+')
print(' '*(left + 3) + '|' + ' ' *input_len + '|')
print(' '*(left + 3) + '|' + input_val + '|')
print(' '* (left + 3) + '|' + ' '*input_len + '|' )
print(' '*left + "+" + '-' *(box_width - 2) + '+')

