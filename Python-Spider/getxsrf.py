#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# get some useful message

import re
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

