#！/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'weekend27'

# string test module

s = 'Python中文，你要好好加油！'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
