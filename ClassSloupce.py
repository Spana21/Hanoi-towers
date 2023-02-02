from Vykresleni import *
# stick object
class Stick(turtle.Turtle):
    """A class that represents a stick for the Tower of Hanoi game.
    Attributes:
                x (int): The x-coordinate of the stick.
                count (int): The number of discs on the stick.
                pos_list (List[int]): A list of y-coordinates for each disc on the stick.
                discs (List[Turtle]): A list of turtle objects that represent the discs on the stick.
        """
    def __init__(self, x):
        """
            Initialize a stick object.

            Parameters:
            x (int): The x-coordinate of the stick.

            Returns:
            None
            """
        super().__init__(shape='square')
        self.x = x
        self.up()
        self.color('grey')
        self.shapesize(10, 1)
        self.goto(self.x, -100)
        self.count = 0
        self.pos_list = [-180, -160, -140, -120, -100, -80, -60, -40]
        self.discs = []


s1 = Stick(-200)
s2 = Stick(0)
s3 = Stick(200)
s4 = Stick(400)