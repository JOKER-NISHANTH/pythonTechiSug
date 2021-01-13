# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:20:05 2021

@author: Nishanth
"""

from firstclassfunction import isodd

n = int(input("Enter the number : "))

res = isodd(n)

if res != None:
    print(res)




List = [1,2,3,4,5,6,7,8,9]

res = isodd(List)

if res != None:
    print(res)





'''
First class function

Function takes any function as argument

'''



def myfunc(func,List):
    res = []
    for item in List:
        val=func(item)
        if val != None:
            res.append(val)
    return res


List = [1,2,3,4,5,6,7,8,9]

res = myfunc(isodd,List)

print(res)




