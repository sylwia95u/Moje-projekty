# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11  20:14:19 2020

@author: Sylwia Urban
"""
class Pytanie:
    def __init__(self, pytanie, odpA, odpB, odpC, odpD, poprawna):
        self.TrescPytania = pytanie
        self.A = odpA
        self.B = odpB
        self.C = odpC
        self.D = odpD
        self.ans = poprawna
        self.guess = ""
        self.ok = False
        self.ZadajPytanie()

    def SprawdzOdpowiedz(self):
        if (self.guess == self.ans):
            print("Poprawna odpowiedź ✔!")
        else:
            print("Błędna odpowiedź ✘")

    def ZadajPytanie(self):
        print(self.TrescPytania)
        print("A) {}".format(self.A))
        print("B) {}".format(self.B))
        print("C) {}".format(self.C))
        print("D) {}".format(self.D))
        self.guess = input("Twoja odpowiedź: ")
        self.SprawdzOdpowiedz()

#tutaj moze dodac sobie pytania wg wzoru p1("tresc", "a", "b", "c", "d", "poprawna")
pytanie1 = Pytanie("Co pije krowa?", "Mleko", "Cola", "Woda", "Fanta", "C")

print("Koniec quizu!")