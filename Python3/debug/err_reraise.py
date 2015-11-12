# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = "weekend27"

# error reraise

def foo(s):
    n = int(s)
    if n == 0:
        return ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
