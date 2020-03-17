#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""
猜密码，二位数字，可以一个一个破解，破解一个就可以得到反馈
界面输入密码，2~6位
"""

def getPasswd():
    passwd = "" # 暂存用户输入的变量
    while True:
        # 接收界面输入，去除前后空格
        passwd = input("Please input your passwd number(0~9), width(2~6)").strip()

        # 确保输入全部是数字,否则重新输入
        if not passwd.isdigit():
            print("Please input correct number,and write again")
        else:
            break
    return passwd

def gassProcess(passwd):
    # 获取用户输入的密码长度，进行for循环遍历
    pwdLen = len(str(passwd))
    pwdList = []

    for index in range(pwdLen):
        pwd = gassSingleNumber(passwd[index])
        pwdList.append(pwd)
    return ''.join(pwdList)

def gassSingleNumber(pwd):
    # 代码写到这里发现这个需求不成立，因为如果密码可以拆分一个一个猜测，
    # 那么直接顺序按照0~9猜测就可以了，也不需要使用什么二分法了。
    # 这就是一个典型的开始构想的需求在开发过程中验证是不成立的
    # 项目放弃
    pass

def gasspasswd():
    passwd = getPasswd()
    gasspwd = gassProcess(passwd)
    print(passwd, gasswd)

