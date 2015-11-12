# -*- coding:utf-8 -*-
#! /bin/env python3    

__author__ = 'weekend27'

# logging debug

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
