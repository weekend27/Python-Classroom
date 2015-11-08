# -*- coding:utf-8 -*-
#! /bin/env python3

'a UDP server test module'     

__author__ = 'weekend27'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 7777))

print('Bind UDP on 7777...')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)
    # s.sendto(data, addr)
