# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:29:50 2023

@author: Khushi
"""

terms = int(input("Enter the number of terms to be displayed : "))
n1 , n2 = 0,1
count = 0

if terms <= 0 :
    print("Invalid number, Please enter positive number")
    
elif terms == 1 :
    print("Fibonacci sequence upto" , nterms, ":")
    print(n1)
    
else :
    print("Fibonacci Sequence :")
    while count < terms :
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1
        
        