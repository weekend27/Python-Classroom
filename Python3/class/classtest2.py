#！/usr/bin/env python3
# -*- coding: utf-8 -*-

'a class module'     

__author__ = 'weekend27'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 55)
yoga = Student('Yoga Weekend', 65)

bart.print_score()
yoga.print_score()
