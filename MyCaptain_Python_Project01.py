# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:15:33 2023

@author: Khushi
"""

#TASK1

Radius = float(input("Enter the radius of the Circle : "))

Area = 3.14159 * Radius * Radius

print("The area of given cirle is :", Area)




#TASK2

File_name = input("Enter the File name : ")

File_ext = File_name.split(".")

print("The extension of the file is :", repr(File_ext[-1]))

