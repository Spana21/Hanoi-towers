from Models.ClassDisky import *
from Models.Sloupce import *


def main():

    number = int(input("Kolik disku? (max 7): "))
    pocet = int(input("Kolik sloupcu?(3 nebo 4): "))


    Disky(number)

    if pocet == 3:
        sloupec = int(input("Na ktery sloupec? (2 nebo 3): "))
        win = turtle.Screen()
        run_turtle(win)
        Sloupce3(sloupec,number)


    if pocet == 4:
        sloupec = int(input("Na ktery sloupec? (2, 3 nebo 4): "))
        win = turtle.Screen()
        run_turtle(win)
        Sloupce4(sloupec,number)

    turtle.done() #okno se po animace nezavre


if __name__ == '__main__':
    main()


