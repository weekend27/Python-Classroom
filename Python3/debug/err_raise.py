# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = "weekend27"

# error raise

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' %s)
    return 10 / n

foo('0')
