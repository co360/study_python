#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""
猜数字，灵活定义数字的上下限
输入一个在upper/lower范围内的值，电脑猜测并给出猜测过程
"""

def getInput(upper=100,lower=0):
    while True:
        passwd = input("please input your passwd: ")
        if passwd.isdigit():
            passwd = int(passwd)
            if upper < passwd or lower > passwd:
                print("Please input value should between %d ~ %d" % (lower,upper))
            else:
                break
        else:
            print("input error...,please again")
    return passwd

def gassNumber(lower=0,upper=100,middle=0,pwd=0,count=0):
    middle = int((lower + upper)/2)
    count += 1
    result = {
        'lower': lower,
        'upper': upper,
        'middle': middle,
        'pwd': pwd,
        'count': count
    }

    print(result)
    
    if pwd == middle:
        return result
    else:
        if middle > pwd:
            result['upper'] = middle - 1
        else:
            result['lower'] = middle + 1
        gassNumber(**result)
    
def init(upper=100,lower=0):
    passwd = getInput(upper=upper,lower=lower)
    gassNumber(pwd=passwd,upper=upper,lower=lower)

init(upper=999,lower=34)
