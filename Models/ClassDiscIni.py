from Models.Vykresleni import *

# Disc object
class Disc(turtle.Turtle):
    def __init__(self, x, y, size, color):
        super().__init__(shape='square')
        self.x = x
        self.y = y
        self.size = size
        self.color(color)
        self.up()
        self.shapesize(1, self.size)
        self.goto(self.x, self.y)
