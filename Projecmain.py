# import the pohyb module from the Source package
from Source.pohyb import *

# Get user input for the number of discs and the destination column
number = int(input("Kolik disku (max 7): "))
sloupec = int(input("Na ktery sloupec (2 nebo 3): "))

# Create Disc objects with specific properties based on the number of discs input
if number == 2:
    # create 2 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    s1.discs = [disc1, disc2]
elif number == 3:
    # create 3 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    s1.discs = [disc1, disc2, disc3]
elif number == 4:
    # create 4 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    s1.discs = [disc1, disc2, disc3, disc4]
elif number == 5:
    # create 5 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    s1.discs = [disc1, disc2, disc3, disc4, disc5]
elif number == 6:
    # create 6 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    disc6 = Disc(-200, -80, 3.5, 'purple')
    s1.discs = [disc1, disc2, disc3, disc4, disc5, disc6]
else:
    # create 7 Disc objects
    disc1 = Disc(-200, -180, 11, 'orange')
    disc2 = Disc(-200, -160, 9.5, 'blue')
    disc3 = Disc(-200, -140, 8, 'red')
    disc4 = Disc(-200, -120, 6.5, 'yellow')
    disc5 = Disc(-200, -100, 5, 'green')
    disc6 = Disc(-200, -80, 3.5, 'purple')
    disc7 = Disc(-200, -60, 2, 'pink')
    number = 7
    s1.discs = [disc1, disc2, disc3, disc4, disc5, disc6, disc7]

s1.count = number

if sloupec == 3:
    hanoi(number, 'A', 'B', 'C')
elif sloupec == 2:
    hanoi(number, 'A', 'C', 'B')
else:
    print("Sloupec neexistje")