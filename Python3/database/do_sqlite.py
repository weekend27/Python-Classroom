#！/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'weekend27'

# sqlite test

import sqlite3

# 连接到SQLite数据库
# 数据库文件是sqlite_test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('sqlite_test.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Weekend\')')
cursor.execute('insert into user (id, name) values (\'2\', \'Yoga\')')
cursor.execute('insert into user (id, name) values (\'3\', \'Halo\')')
# 通过rowcount获得插入的行数
print('rowcount =', cursor.rowcount)
# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()

# 查询记录
conn = sqlite3.connect('sqlite_test.db')
cursor = conn.cursor()
# 执行查询语句
# cursor.execute('select * from user where id=?', '1')
# cursor.execute('select * from user where id=?', '2')
cursor.execute('select * from user where id=?', '3')
# 获得查询结果
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
