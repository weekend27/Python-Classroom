# -*- coding:utf-8 -*-
#! /bin/env python3

'a TCP client test module'     

__author__ = 'weekend27'

import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.connect(('127.0.0.1', 9999))

# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Weekend', b'Tracy', b'Yoga']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
