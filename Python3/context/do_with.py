#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# do with

from contextlib import contextmanager

@contextmanager
def log(name):
    print('[%s] start...' % name)
    yield
    print('[%s] end.' % name)

with log('DEBUG'):
    print('Hello, world!')
    print('Hello, Python!')
