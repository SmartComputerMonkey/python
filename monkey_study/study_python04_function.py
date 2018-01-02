#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Monkey"

#集合操作
#作用
#1、去重，把一个列表变成集合，就自动去重了  无序
list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)
print(list_1,type(list_1))
#2、关系测试，测试两组数据之前的交集、差集、并集等关系
list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)
#取交集
print(list_1.intersection(list_2))
#取并集
print(list_1.union(list_2))
#取差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))
#子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
print(list_1.issubset(list_3))
#对称差集
print(list_1.symmric_difference(list_2))
print("-------------------------------")
#两集合没有交集  返回true
list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))
#函数基本语法及特性
#参数与局部变量
#返回值
#递归
#匿名函数
#函数式编程介绍
#高阶函数
#内置函数
