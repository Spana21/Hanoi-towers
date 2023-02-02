from Vykresleni import *
# Disc object
class Disc(turtle.Turtle):
    """
    This class creates an instance of a disc in the Tower of Hanoi game.

    Parameters:
    x (int): The x-coordinate of the disc.
    y (int): The y-coordinate of the disc.
    size (int): The size of the disc.
    color (str): The color of the disc.

    Attributes:
    x (int): The x-coordinate of the disc.
    y (int): The y-coordinate of the disc.
    size (int): The size of the disc.
    """
    def __init__(self, x, y, size, color):
        super().__init__(shape='square')
        self.x = x
        self.y = y
        self.size = size
        self.color(color)
        self.up()
        self.shapesize(1, self.size)
        self.goto(self.x, self.y)