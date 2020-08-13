# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:15:33 2020

@author: Saptarshi
"""

import sympy
import math

n = int(input())
a=math.floor(n/2)

sum =0
count = 0
arr = []
arr = list(sympy.primerange(0, a))
for i in arr:
    sum = sum+int(i)
    if (sympy.isprime(sum)):
        count+=1
        

print(count-1)