#！/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'weekend27'

# dict test module

d = {
    'Weekend': 99,
    'Yoga': 94,
    'Seapub': 96
    }
print('d[\'Weekend\'] =', d['Weekend'])
print('d[\'Yoga\'] =', d['Yoga'])
print('d[\'Seapub\'] =', d['Seapub'])

# if there is no key that you want to access...
print('d.get(\'Little\', -1) =', d.get('Little', -1))
