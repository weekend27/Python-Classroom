#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!!!'

print re.subn(pattern, r'\2 \1', s)

def func(m):
	return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern, func, s)

### output ###
# ('say i, world hello!!!', 2)
# ('I Say, Hello World!!!', 2)
