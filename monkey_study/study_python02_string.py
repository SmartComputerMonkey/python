#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Monkey"

# 字符串 练习
name = "my name is {name},age is {age}"
print(name.capitalize())
print(name.count("m"))
print(name.center(50,"-")) #打印50个字符  name放中间
print(name.encode()) #字符串转2进制
print(name.endswith("ey"))
name1 = "my \tname is monkey"
print(name1.expandtabs(tabsize=30))
print(name.find("name"))
print(name[name.find("name")])#字符串也可以切片
print(name.format(name='monkey',age='25'))
print(name.format_map({'name':'monkey','age':25}))
print(name.isalnum())#b包含数字
print(name.isalpha())#包含大小
print(name.isdecimal())#是十进制
print(name.isdigit())#是一个整数
print(name.isidentifier())#判断是不是一个合法的标示符
print(name.islower())#是不是一个小写
print(name.isnumeric())#判断是不是一个合法的标示符
print(name.isspace())#判断是不是一个空格
print(name.istitle())#判断是不是一个题目
print(name.isprintable())#是不是可以打印 tty file  drive file
print(name.isupper())
print(name.islower())
print(''.join(['1','2','3','4']))#将列表转为字符串
print('+'.join(['1','2','3','4']))#将列表转为字符串
print(name.ljust(50,'*'))
print(name.rjust(50,'-'))
print("Alex".lower())
print("monkey".upper())
print("Alex\n".lstrip())#去掉左边的空格和回车
print("\nAlex\n".rstrip())
print("\nAlex\n".strip())#去掉两边的空格和回车
p = str.maketrans("monkey","yeknom")
print("ooooo".translate(p)) #加密
print('monkey'.replace('k','K',1))
print('monkeye'.rfind('e'))#返回出现字符最大角标的值
print("monkeylll ooo pp".split())#切分
print("1+2\n+3+4".splitlines())
print("Mr Monkey".swapcase())
print("Monkey".title())
print("lex li".zfill(50))
