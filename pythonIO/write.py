#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("test.txt", "wb")
f.write("duangduang\nhuanghuang\n")

f.close()

'''
输出结果：
$ cat test.txt
duangduang
huanghuang
'''
