# -*- coding: utf-8 -*-
 """
Created on Sat Feb 11 00:43:16 2023

@author: Khushi
"""
#task_1
Radius=float(input("Enter the radius of the circle :"))
Area_of_circle = 3.14*Radius*Radius
print("The area of the cirlse is ", Area_of_circle)



#task_2
filename=input("Enter the Filename: ")
f_ext= filename.split(".")
print("The Extension of the file is : " + repr(f_ext[-1]))
