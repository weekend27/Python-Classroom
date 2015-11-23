#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!!!'

print re.sub(pattern, r'\2 \1', s)

def func(m):
	return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern, func, s)

### output ###
# say i, world hello!!!
# I Say, Hello World!!!