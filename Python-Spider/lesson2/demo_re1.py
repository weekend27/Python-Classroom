#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

'''
# return pattern object
re.compile(string[,flag])

# match functions
re.match(pattern, string[, flag])
re.search(pattern, string[, flags])
re.split(pattern, string[, maxsplit])
re.findall(pattern, string[, flags])
re.finditer(pattern, string[, flags])
re.sub(pattern, repl, string[, count])
re.subn(pattern, repl, string[, count])
'''

pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo hwj!')
result3 = re.match(pattern, 'helo hwj!')
result4 = re.match(pattern, 'hello hwj!')

if result1:
    print result1.group()
else:
    print '1 match failed!!!'

if result2:
    print result2.group()
else:
    print '2 match failed!!!'

if result3:
    print result3.group()
else:
    print '3 match failed!!!'

if result4:
    print result4.group()
else:
    print '4 match failed!!!'
