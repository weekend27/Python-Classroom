#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("print.py", "wb")
print "file name:", f.name
print "close or not:", f.closed
print "access mode:", f.mode
print "must append a space:", f.softspace

'''
输出结果：
file name: print.py
close or not: False
access mode: wb
must append a space: 0
'''
