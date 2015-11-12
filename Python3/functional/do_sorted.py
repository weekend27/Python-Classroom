#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# sorted

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 74), ('Adam', 98), ('Baonel',89), ('Weekend27',100)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
