# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = "weekend27"

# do try

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
