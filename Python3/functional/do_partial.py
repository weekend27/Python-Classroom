#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# partial function
# number change base

import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int10 = functools.partial(int, base=10)
int16 = functools.partial(int, base=16)

print('10 =', int2('10'))
print('1000000 =', int2('1000000'))
print('20 =', int8('20'))
print('1234567 =', int8('1234567'))
print('20 =', int10('20'))
print('4455397 =', int10('4455397'))
print('20 =', int16('20'))
print('fffffff =', int16('fffffff'))

