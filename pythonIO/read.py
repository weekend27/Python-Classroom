#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("test.txt", "r+")
str = f.read(14)
print "string:", str

f.close()


'''
输出结果：(注意：换行符\n也是一个字节)
string: duangduang
hua
'''
