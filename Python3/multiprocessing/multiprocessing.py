# -*- coding:utf-8 -*-
#! /bin/env python3

'a multiprocessing module'     

__author__ = 'weekend27'

import os

print('Process (%s) start...' % os.getpid())
#Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    
