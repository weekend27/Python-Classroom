# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = 'weekend27'

# recursion

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(100) =', fact(100))

# 利用递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)

move(20, 'A', 'B', 'C') # run over 90 seconds on my machine
