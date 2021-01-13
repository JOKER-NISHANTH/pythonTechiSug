# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:53:56 2021

@author: Nishanth
"""

'''
Closure

Nested Function

'''


def outer(): # 2
    x = 5 # 3
    def inner(): #5
        print(x) # 6
    inner() # 4

#inner() # NameError: name 'inner' is not defined ;
#  inner() - error local function can't call outside function body

outer() # 1






def sam():
    print("Hello")

sam()

obj = sam # sam function object id it's store in obj variable

# This method is used for access the inner function from outside the function block
print(obj)
obj()






# access the inner function

def outer(): # 2
    x = 5 # 3
    def inner(): #5
        print(x) # 6

    return inner() # 4

obj_id  = outer() # 1
print(obj_id)







def outer():
    x = 5
    def inner():
        y = 5
        res = x + y
        return res
    return inner()

obj_id = outer()
print(obj_id)







'''
What is closure ?

    Function object that remembers values in the enclosing scope
even if they are not present in memory.

'''

# even after finishing the execution of outer function the msg "Python"

def outer(): # 2
    msg = "Python" # 3
    def inner(): # 5
        print(msg) # 6
    return inner # 4    # here return inner object ID

obj = outer() # 1
obj()




