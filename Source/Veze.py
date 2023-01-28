import turtle

# screen object
win = turtle.Screen()
win.setup(800, 600)
win.title('Hanoiske vezee')
win.tracer(0) # aby se to hned vsechno vykreslilo

# base object
base = turtle.Turtle()
base.color('gray') # color
base.shape('square')
base.goto(0, -200)  # souradnice
base.shapesize(1, 35)

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

# stick
s1 = Stick(-200)
s2 = Stick(0)
s3 = Stick(200)