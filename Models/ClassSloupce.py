from Projekt.Models.Vykresleni import *

# stick object
class Stick(turtle.Turtle):
    def __init__(self, x):
        super().__init__(shape='square') # z turtle kopiruje shape
        self.x = x
        self.up()
        self.color('grey')
        self.shapesize(10, 1)
        self.goto(self.x, -100)
        self.count = 0
        self.pos_list = [-180, -160, -140, -120, -100, -80, -60, -40]  # pozice na tyckach, kde se budou disky zastavovat
        self.discs = []


s1 = Stick(-200)
s2 = Stick(0)
s3 = Stick(200)
s4 = Stick(400)