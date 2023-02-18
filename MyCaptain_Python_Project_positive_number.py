# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:18:19 2023

@author: Khushi
"""

start = int(input("Enter the starting number of the range : "))
end = int(input("Enter the ending number of the range : "))

print("Positive Numbers in the range", start, "to", end, "are:")

for i in range(start, end + 1):
    if i > 0 :
        print(i)
        