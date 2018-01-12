#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

n = 32
f = 4325.564
s1 = 'hello, world'
s2 = 'hello, \'Jin\''
s3 = r'hello, "Jin"'
s4 = r'''hello,
Jin!
das'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
print("你好啊")

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
