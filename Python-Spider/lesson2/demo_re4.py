#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

pattern = re.compile(r'\d+')
print re.split(pattern, 'one1two2three3four4')

### output ###
# ['one', 'two', 'three', 'four', '']