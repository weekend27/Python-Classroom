#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "weekend27"

# test queue

from collections import deque

queue = deque(['yoga','weekend','halo'])
queue.append('Jerry')
queue.append('Kobe')
queue.popleft()   # 队首元素出队
# output 'yoga'
queue.popleft()   # 队首元素出队
# output 'weekend'
print(queue)
# output deque(['halo', 'Jerry', 'Kobe'])
