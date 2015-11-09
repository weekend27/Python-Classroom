#！/usr/bin/env python3
# -*- coding: utf-8 -*-

'a class module'     

__author__ = 'weekend27'

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating KFC...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def sleep(self):
        print('Cat is sleeping...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.sleep()
