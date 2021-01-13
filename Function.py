# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:44:55 2021

@author: Nishanth
"""


# Nested function


def outerfun(): # 2
    oname = "BlackPearl" # 3
    def innerfun(): # 5
        iname = "Cyber King" # 6
        print(iname) # 7   ; 1st print
    innerfun() # 4
    print(oname) # 8   ; 2nd print
outerfun() # 1















