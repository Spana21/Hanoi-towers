from Projekt.Models.Pohyb import *

def Disky(number):
    if number == 2:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        s1.discs = [disc1, disc2]
    elif number == 3:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        disc3 = Disc(-200, -140, 8, 'red')
        s1.discs = [disc1, disc2, disc3]
    elif number == 4:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        disc3 = Disc(-200, -140, 8, 'red')
        disc4 = Disc(-200, -120, 6.5, 'yellow')
        s1.discs = [disc1, disc2, disc3, disc4]
    elif number == 5:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        disc3 = Disc(-200, -140, 8, 'red')
        disc4 = Disc(-200, -120, 6.5, 'yellow')
        disc5 = Disc(-200, -100, 5, 'green')
        s1.discs = [disc1, disc2, disc3, disc4, disc5]
    elif number == 6:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        disc3 = Disc(-200, -140, 8, 'red')
        disc4 = Disc(-200, -120, 6.5, 'yellow')
        disc5 = Disc(-200, -100, 5, 'green')
        disc6 = Disc(-200, -80, 3.5, 'purple')
        s1.discs = [disc1, disc2, disc3, disc4, disc5, disc6]
    elif number == 7:
        disc1 = Disc(-200, -180, 11, 'orange')
        disc2 = Disc(-200, -160, 9.5, 'blue')
        disc3 = Disc(-200, -140, 8, 'red')
        disc4 = Disc(-200, -120, 6.5, 'yellow')
        disc5 = Disc(-200, -100, 5, 'green')
        disc6 = Disc(-200, -80, 3.5, 'purple')
        disc7 = Disc(-200, -60, 2, 'pink')
        s1.discs = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

    s1.count = number