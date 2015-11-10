# -*- coding:utf-8 -*-
#! /bin/env python3   

__author__ = 'weekend27'

# if test

grade = int(input('Input your grade: '))

if grade >= 90:
    print('Really perfect job!')
elif grade >= 80:
    print('You have done a good job!')
elif grade >= 70:
    print('You should try your best!')
else:
    print('Goodbye!')
