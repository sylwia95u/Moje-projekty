# -*- coding: utf-8 -*-
"""
Created on Thu Jan 2  16:08:33 2020

@author: Sylwia Urban
"""
import random

liczba = random.randint(0, 100)
print("Wpadłeś w moją pułapkę! Porwałam Cię do innego świata!", )
print("Aby się uwolnić odgadnij liczbę o jakiej pomyślałam!")
print()
print("podaj liczbę z zakresu 0-100")
while True:
    wczytana = int(input())
    #print(wczytana)
    roznica = liczba - wczytana
    if roznica == 0:
        print("Gratulacje, odgadłeś liczbę!")
        break
    elif roznica >= -5 != roznica <= 5:
        print("Jesteś blisko, próbuj dalej!")
    elif wczytana > liczba:
        print("Zbyt duża liczba, próbuj dalej")
    elif wczytana < liczba:
        print("Zbyt mała liczba, próbuj dalej")
