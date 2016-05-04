#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件并读取文件
f = open("test.txt", "r+")
str = f.read(14)
print "string:", str

# 获取指针当前位置
pos = f.tell()
print "current position:", pos
str = f.read(14)
print "string:", str

# 重新将指针定位到文件开头
pos = f.seek(0, 0)
str = f.read(14)
print "string:", str


f.close()


'''
输出结果：
string: duangduang
hua
current position: 14
string: nghuang

string: duangduang
hua
'''
