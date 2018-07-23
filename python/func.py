#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:29:37 2018

@author: aaronfernandez
"""





chance = int(input("enter your chances"))

def prime_or_not():
    for attempt in  range(chance):
        num = int(input('Enter your number'))
   
        if num > 1:

            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    break
                else:
                    print(num,"is a prime number")
       
        else:
            print(num,"is not a prime number")
        

prime_or_not()