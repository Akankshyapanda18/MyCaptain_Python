# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 00:20:44 2023

@author: Khushi
"""
def positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0 :
            positive_numbers.append(num)
    print(positive_numbers)

list1 = [12, -7 , 5, 64, -14]
list2 = [12, 14, -95, 3]
positive_numbers(list1)
positive_numbers(list2)
