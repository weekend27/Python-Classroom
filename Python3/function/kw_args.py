# -*- coding: utf-8 -*-
#! /usr/bin/env python3

__author__ = "weekend27"

# key-word args

def print_scores(**kw):
    print('     Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data={
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)

def print_info(name, *, gender, city='Singapore', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob', gender='male', age=88)
print_info('Mary', gender='female', city='Shanghai', age=58)
