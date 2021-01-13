# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:55:01 2021

@author: Nishanth
"""


"""

Any Python callable object that is used to modify a function or a class

    1. Function Decorator
    2. Class Decorator


Fucntion Decorator:
1. Nested function
2. Function can return another function
3. Function are reference
4. Function are parameter


"""


'''
Previous Example

1. Nested function
2. Function can return another function
3. Function are reference

'''

def outer(): # 2
    n1 = 3 # 3
    def inner(): # 5
        n2 = 6 # 6
        res = n1 + n2 # 7
        return res # 8
    return inner # 4 # Function are reference

inner_obj = outer() # 1
inner_obj()

# To check the inner_obj is denote the  inner function

print(inner_obj.__name__)


# =====================================================

'''
 4. Function are parameter

 Passing function as parameter

'''

def func1(): # 4
    print('Hai am function 1') # 5

def func2(fun): # 1
    print('Hai am Function 2 ........ Calling Fucntion 1') # 2
    fun() # 3

func2(func1)



# =====================================================
# Implement the decorators without parameter


def strupper(func) -> str:
    def inner():
        str1 = func() # hai welcome !!!
        return str1.upper() # HAI WELCOME!!!
    return inner

def greet() -> str:
    return "hai welcome !!!"


print(greet()) # Display Uppercase

obj = strupper(greet) # Passing function as reference
print(obj())




def strupper(func) -> str:
    def inner():
        str1 = func() # hai welcome !!!
        return str1.upper() # HAI WELCOME!!!
    return inner

@strupper
def greet() -> str:
    return "hai welcome !!!"


print(greet()) # Display Uppercase

obj = strupper(greet) # Passing function as reference
print(obj())


'''
Dectorator with parameter

'''

def div(a,b):
    return a / b

print(div(4,0))




def divdec(func):
    def inner(x,y):
        if y == 0:
            return "Give value greater than zero"
        return func(x,y)
    return inner

@divdec
def div(a,b):
    return a / b

print(div(4,0))
print(div(4,2))



'''
    Decorator

    1. Need to take function as parameter
    2. Add Functionality to function
    3. Function need to return another function

'''








# =====================================================


'''
Now we see

1. Single Function with multiple decorators
2. Decorator with parameter
3. Multiple Function with Single Decorator

'''

# Single Function with single decorators

def sample():
    return " hello welcome "

print(sample())


def upperstr(func_name): #func_name = sample
    def inner():
        up = func_name()
        return up.upper()
    return inner

@upperstr
def sample():
    return " hello welcome "

print(sample())
obj = sample
print(obj())











# Single Function with multiple decorators


def upperstr(func_name): #func_name = sample
    def inner():
        up = func_name()
        return up.upper()
    return inner


def splitstr(func):
    def inner():
        Split = func()
        return Split.split()
    return inner


@splitstr # 2
@upperstr # 1
def sample():
    return "hello welcome"

print(sample())
obj = sample
print(obj())




# =========================================

# Decorator with parameter

# output hello welcome !! <name>

def outer(decarg):  # decarg receive Decorator parameter
    def upperstr(func):
        def inner():
            return func() + decarg
        return inner
    return upperstr

@outer(" BlackPearl ")
def sample():
    return "hello world"

print(sample())



#  =====================================

# Multiple Function with single decorator another name is general decorator



def divdec(func):
    def inner(*args):
        if 0 in args[1:]:
            return "Enter the non-zero value"
        return func(*args)
    return inner


@divdec
def div1(x,y):
    return x / y

@divdec
def div2(a,b,c):
    return a / b / c

print(div1(20,2))
print(div1(20,0))
print(div2(30,0,5))
print(div2(30,3,5))
































