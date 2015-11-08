# -*- coding:utf-8 -*-
#! /bin/env python3

'a UDP client test module'     

__author__ = 'weekend27'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Face++', b'Sensetime', b'Zhihu']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 7777))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()
