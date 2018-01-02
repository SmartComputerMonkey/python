#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Monkey"

#购物车例子
#需求 1、启动程序后，让用户输入工资，然后打印商品列表
#     2、允许用户根据商品编号购买商品
#     3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#     4、可随时退出，退出时，打印已购买商品和余额

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('book',120),
]
shopping_list = []
salary = input("Input your salary:")

# enumerate 把列表的下标找出来
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("choice>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is %s" %(p_item,salary))
        elif user_choice == 'q':
            print("exit....")
        else:
            print("invalid option")
