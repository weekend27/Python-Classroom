#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# post

import http.cookiejar
import urllib.request
def getOpener(head):
    # deal with the Cookie
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
