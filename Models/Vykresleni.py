import turtle # kresleni

def run_turtle(win):
    win.setup(1200, 600)
    win.title('Hanoiske vezee')
    win.tracer(0)  # aby se to hned vsechno vykreslilo


    # base object
    base = turtle.Turtle()
    base.color('gray')  # color
    base.shape('square')
    base.goto(0, -200)  # souradnice
    base.shapesize(1, 45)

def update_turtle():
    win = turtle.Screen()
    win.update()






