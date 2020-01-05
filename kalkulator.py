# -*- coding: utf-8 -*-
"""
Created on Sat Dec  28 18:41:56 2019

@author: Sylwia Urban
"""

def dodawanie(x, y):
   return x + y
def odejmowanie(x, y):
   return x - y
def mnożenie(x, y):
   return x * y
def dzielenie(x, y):
   return x / y
num1 = float(input("Wprowadź pierwszą liczbę: "))
num2 = float(input("Wprowadź drugą liczbę: "))
print("Wybierz operację:")
print("1.Dodawanie")
print("2.Odejmowaie")
print("3.Mnożenie")
print("4.Dzielenie")
choice = input("Wybierz numer operacji(1/2/3/4): ")
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")