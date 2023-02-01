from Projekt.Models.Pohyb import *


def Sloupce4(sloupec, number):
    if sloupec == 4:
        hanoi4(number, 'A', 'B', 'C', 'D')
    elif sloupec == 3:
        hanoi4(number, 'A', 'B', 'D', 'C')
    elif sloupec == 2:
        hanoi4(number, 'A', 'C', 'D', 'B')
    else:
        print("Sloupec neexistje")


def Sloupce3(sloupec, number):
    if sloupec == 3:
        hanoi3(number, 'A', 'B', 'C')
    elif sloupec == 2:
        hanoi3(number, 'A', 'C', 'B')
    else:
        print("Sloupec neexistje")
