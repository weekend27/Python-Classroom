# -*- coding:utf-8 -*-
#! /bin/env python3  

__author__ = 'weekend27'

#bubble sort

array = [1,2,5,3,6,8,4]
print('The original array:')
print(array)
print('***bubble sort start***')
for i in range(len(array) - 1, 0, -1):
    print('i = ', i)
    for j in range(0, i):
        # print(j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print('Yes Exchange between ', j, ' and ', j + 1, '...')
            print(array)
        else:
            print('No! Exchange between ', j, ' and ', j + 1, '...')

print('***bubble sort stop***')
print('The final result:')
print(array)
