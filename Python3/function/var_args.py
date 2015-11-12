# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = 'weekend27'

# variable args

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi')   # => greeting='Hi', args=()
hello('Hi', 'Johnson')   # => greeting='Hi', args=('Johnson')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Lory', 'Tensa')
hello('Hello', *names)  # =>greeting='Hello', args=('Lory', 'Tensa')
