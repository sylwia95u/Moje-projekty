# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12  22:00:24 2019

@author: Sylwia Urban
"""
print('▲▲▲ Obliczanie pola trójkąta przy użyciu wzoru Herona ▲▲▲')
a = float(input('Podaj długość pierwszego boku: '))
b = float(input('Podaj długość drugiego boku: '))
c = float(input('Podaj długość trzeciego boku: '))
s = (a + b + c) / 2
pole = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('Pole trójkąta jest równe %0.2f' %pole)