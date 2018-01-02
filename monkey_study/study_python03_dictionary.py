#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Monkey"

#字典的使用  类似于java map集合
info = {
    'student01':'monkey king',
    'student02':'beautiful monkey',
    'student03':'monkey'
}
#查找
print(info.get('student04'))
print('student04' in info)#info.has_key("student04") 2.版本
'''
print(info)#字典无序  打印  无序打印
print(info['student01'])
info['student01'] = "KK"
print(info['student01'])
info['student04'] = "monkey4"
print(info)
#del
del info["student01"]
info.pop("student02")
info.popitem()#随机删
'''
#多级字典嵌套及操作
b = {
    "student01":"KK",
    1:3,
    2:5
}
info.update(b)#合并两个字典
print(info)
print(info.items())#字典转列表
c = dict.fromkeys([6,7,8],"test")#初始化一个新的字典
print(c)

#字典的循环
#高效
for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)