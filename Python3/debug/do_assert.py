# -*- coding:utf-8 -*-
#! /bin/env python3    

__author__ = 'weekend27'

# assert debug

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!!!!!!!!'
    return 10 / n

def main():
    foo('0')

main()
