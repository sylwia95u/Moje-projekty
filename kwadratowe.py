# -*- coding: utf-8 -*-
"""
Created on Tue Jan  14 22:41:56 2020

@author: Sylwia Urban
"""
import math

print("Program znajdujący pierwiastki równania kwadratowego typu y = ax^2 + bx + c")

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

print("Podane wartości:\ta={}, b={}, c={}".format(a,b,c))

delta = b**2 - 4 * a * c
print("Delta:\t{}".format(delta))

if (delta == 0):
    x = (-1 * b) / (2 * a)
    print("Równanie ma jedno rozwiązanie x = {}, pierwiastek podwójny".format(x))
elif (delta > 0):
    x1 = (-1 * b - math.sqrt(delta)) / (2 * a)
    x2 = (-1 * b + math.sqrt(delta)) / (2 * a)
    print("Równanie ma dwa rozwiązania x1 = {}, x2 = {}".format(x1, x2))
else:
    print("Równanie nie ma rozwiązań rzeczywistych, delta ujemna")