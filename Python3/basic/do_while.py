# -*- coding:utf-8 -*-
#! /bin/env python3

'while test'

__author__ = 'weekend27'

# calculate 1+2+3+...+100
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print('1+2+3+...+100 =', sum)

# calculate 1*2*3*...*100
product = 1
p = 1
while p <= 100:
    product = product * p
    p = p + 1
print('1*2*3*...*100 =', product)
