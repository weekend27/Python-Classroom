#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# ungzip

import gzip
def ungzip(data):
    try:
        print('准备解压……')
        data = gzip.decompress(data)
        print('解压完毕！')
    except:
        print('未经压缩，不需解压！')
    return data

ungzip(b'hello,gzip!')
