# -*- coding:utf-8 -*-
#! /bin/env python3

__author__ = "weekend27"

# error
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
