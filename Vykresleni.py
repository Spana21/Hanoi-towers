# import turtle # kresleni
import turtle

def run_turtle(win):
    """
    This function sets up the turtle window for the Hanoi towers game.
        Parameters:
                    win (turtle.Screen): The turtle screen object.

        Returns:
                None
    """
    win.setup(1200, 600)
    win.title('Hanoiske vezee')
    win.tracer(0)  # aby se to hned vsechno vykreslilo


def update_turtle():
    """
       This function updates the turtle screen to display the current state of the simulation.
    """
    win = turtle.Screen()
    win.update()

def base():
    """
      This function creates the base of the tower.
      The base is a square shaped turtle object with gray color.
      The base is located at coordinates (0, -200) and its height is 45.
    """
    import turtle
    base = turtle.Turtle()
    base.color('gray')  # color
    base.shape('square')
    base.goto(0, -200)  # souradnice
    base.shapesize(1, 45)




