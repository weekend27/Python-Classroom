#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = "weekend27"

import re

pattern = re.compile(r'\d+')
for m in re.finditer(pattern, 'one1two2three3four4'):
	print m.group(),    # surprise!!! add ',' can make multi-lines to sigle-line

### output ###
# 1 2 3 4