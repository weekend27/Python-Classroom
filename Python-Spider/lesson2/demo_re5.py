#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

pattern = re.compile(r'\d+')
print re.findall(pattern, 'one1two2three3four4')

### output ###
# ['1', '2', '3', '4']