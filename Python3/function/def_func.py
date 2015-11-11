# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = 'weekend27'

# define function

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-90)
print(n)
m = my_abs(70)
print(m)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type
my_abs('678')
