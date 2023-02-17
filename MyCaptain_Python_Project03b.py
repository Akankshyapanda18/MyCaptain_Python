# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:54:29 2023

@author: Khushi
"""

def most_frequent(string) :
    freq = {}
    for letter in string :
        freq[letter] = freq.get(letter, 0) + 1
        
    freq = sorted(freq.items(), key = lambda x : x[1], reverse=True)
    
    for letter, count in freq :
        print(f"{letter} = {count:02d}", end = " ")

most_frequent("Mississippi")