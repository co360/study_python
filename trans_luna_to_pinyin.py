#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@wmsj100>
#
# Distributed under terms of the MIT license.

"""
转换luna的词库
"""
import sys
import os
import json

def deal_line(line):
    cur_line = line.strip()
    if line.startswith('#'):
        return ''

    line_list = cur_line.split()
    if len(line_list) < 3:
        return ''

    pin_yin = "'".join(line_list[1:-1])
    return ' '.join([line_list[0], pin_yin, line_list[-1]])

def write_to_file(result, file_path):
    data = '\n'.join(result)

    with open(file_path + '_out', 'w') as file:
        file.write(data)

def init(file_name):
    file_path = os.path.abspath(file_name)
    if os.path.isfile(file_path):
        result = set()
        with open(file_path, 'r') as file:
            for line in file.readlines():
                target_line = deal_line(line)
                if target_line:
                    result.add(target_line)

        print(result)
        write_to_file(result, file_path)
    else:
        print("file is not exist")

if __name__ == '__main__':
    if len(sys.argv) >1:
        file_name=sys.argv[1]
        init(file_name)
