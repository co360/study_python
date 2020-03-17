#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 wmsj100 <wmsj100@hotmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def excep():
    try:
        x = input('first number')
        y = input('second number')
        print(int(x)/int(y))
    except ZeroDivisionError:
        print('The second number can\'t be zero.')

class Calculate:
    flag = False
    def cals(self, excp):
        try:
            return eval(excp)
        except ZeroDivisionError:
            if self.flag:
                return 'The Second number can\'t be zero'
            else:
                raise
        except TypeError:
            if self.flag:
                return 'Please just input number'
            else:
                raise
        except NameError:
            if self.flag:
                return 'Please make sure param has defined'
            else:
                raise

class Cal1:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError):
            return 'Please input correct number'

class Cal2:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError) as e:
            print(e)

class Cal3:
    flag = False
    def cals(self,exprval):
        try:
            return eval(exprval)
        except (ZeroDivisionError,NameError,TypeError) as e:
            print(e)
        except Exception as e:
            print("other error: %s" % e)

class Cal4:
    def cals(self,exprval):
        while True:
            try:
                print(eval(exprval))
            except Exception as e:
                print("other error: %s" % e)
            else:
                break

class Cal5:
    def cals(self,exprval):
        try:
            return eval(exprval)
        except Exception as e:
            print("other error: %s" % e)
        else:
            print("start planing ,not error")
        finally:
            print("finally!!!")

class Cal6:
    def fault(self):
        raise Exception('Something is error')

    def ignore(self):
        self.fault()
    
    def deal(self):
        try:
            self.fault()
        except:
            print("thsi is some error,please deal")
