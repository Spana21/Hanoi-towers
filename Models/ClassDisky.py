from Projekt.Models.ClassDiscIni import *
from Projekt.Models.ClassSloupce import *

class Disky():
    def __init__(self, number):
        if number == 2:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            s1.discs = [self.disc1, self.disc2]
        elif number == 3:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            self.disc3 = Disc(-200, -140, 8, 'red')
            s1.discs = [self.disc1, self.disc2, self.disc3]
        elif number == 4:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            self.disc3 = Disc(-200, -140, 8, 'red')
            self.disc4 = Disc(-200, -120, 6.5, 'yellow')
            s1.discs = [self.disc1, self.disc2, self.disc3, self.disc4]
        elif number == 5:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            self.disc3 = Disc(-200, -140, 8, 'red')
            self.disc4 = Disc(-200, -120, 6.5, 'yellow')
            self.disc5 = Disc(-200, -100, 5, 'green')
            s1.discs = [self.disc1, self.disc2, self.disc3, self.disc4, self.disc5]
        elif number == 6:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            self.disc3 = Disc(-200, -140, 8, 'red')
            self.disc4 = Disc(-200, -120, 6.5, 'yellow')
            self.disc5 = Disc(-200, -100, 5, 'green')
            self.disc6 = Disc(-200, -80, 3.5, 'purple')
            s1.discs = [self.disc1, self.disc2, self.disc3, self.disc4, self.disc5, self.disc6]
        elif number == 7:
            self.disc1 = Disc(-200, -180, 11, 'orange')
            self.disc2 = Disc(-200, -160, 9.5, 'blue')
            self.disc3 = Disc(-200, -140, 8, 'red')
            self.disc4 = Disc(-200, -120, 6.5, 'yellow')
            self.disc5 = Disc(-200, -100, 5, 'green')
            self.disc6 = Disc(-200, -80, 3.5, 'purple')
            self.disc7 = Disc(-200, -60, 2, 'pink')
            s1.discs = [self.disc1, self.disc2, self.disc3, self.disc4, self.disc5, self.disc6, self.disc7]

        s1.count = number