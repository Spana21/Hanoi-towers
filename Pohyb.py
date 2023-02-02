from ClassSloupce import *
import time


def move_disc(disc, pin):
    """
     This function moves the disc from its current position to the top of the pin.

     Parameters:
     disc (turtle object): The disc that needs to be moved.
     pin (Pin object): The destination pin for the disc.

     Returns:
     None
     """
    while disc.ycor() < 100:
        # move the disc towards the pin
        disc.goto(disc.xcor(), disc.ycor() + 5)
        update_turtle()
    # move the disc to the top of the pin
    disc.goto(pin.xcor(), 100)
    update_turtle()
    while disc.ycor() > pin.pos_list[pin.count]:
        # move the disc to its final position
        disc.goto(disc.xcor(), disc.ycor() - 5)
        update_turtle()
    time.sleep(0.001)  # adjust speed



def move(f, t):
    """
      This function moves a disc from the source `f` pin to the target `t` pin.

      Parameters:
      f (str): The source pin ('A', 'B', 'C', or 'D').
      t (str): The target pin ('A', 'B', 'C', or 'D').

      Returns:
      None
      """
    print(f'Move disc from {f} to {t}!')

    # Assign the source pin based on the input value of f
    if f == 'A':
        top_disc = s1.discs[-1]
        start_pin = s1
    elif f == 'B':
        top_disc = s2.discs[-1]
        start_pin = s2
    elif f == 'C':
        top_disc = s3.discs[-1]
        start_pin = s3
    elif f == 'D':
        top_disc = s4.discs[-1]
        start_pin = s4

    # Assign the target pin based on the input value of t
    if t == 'A':
        s = s1
    elif t == 'B':
        s = s2
    elif t == 'C':
        s = s3
    elif t == 'D':
        s = s4
    # move the top disc from start pin to target pin
    move_disc(top_disc, s)
    # decrement the count of disc on the start pin
    start_pin.count -= 1
    # remove the top disc from the start pin
    start_pin.discs.pop()
    # increment the count of discs on the target pin
    s.count += 1
    # add the top disc to the target pin
    s.discs.append(top_disc)


def hanoi4(n, f, h,k,t):
    """
       This function implements the Tower of Hanoi with 4 columns.

       Parameters:
       n (int): The number of discs in the game.
       f (str): The source pin ('A', 'B', 'C', or 'D').
       h (str): The helper pin ('A', 'B', 'C', or 'D').
       k (str): The helper pin ('A', 'B', 'C', or 'D').
       t (str): The target pin ('A', 'B', 'C', or 'D').

       Returns:
       None
       """
    if n == 0:
        return
    if n == 1:
        move(f,t)
        return

    hanoi4(n - 2, f, k, t,h)
    move(f, k)
    move(f,t)
    move(k,t)
    hanoi4(n - 2, h, k,f, t)

def hanoi3(n,f,h,t):
    """
        This function implements the Tower of Hanoi with 3 columns.

        Parameters:
        n (int): The number of discs in the game.
        f (str): The source pin ('A', 'B', or 'C').
        h (str): The helper pin ('A', 'B', or 'C').
        t (str): The target pin ('A', 'B', or 'C').

        Returns:
        None
        """
    if n == 1:
        move(f,t)
        return
    hanoi3(n-1,f,t,h)
    move(f,t)
    hanoi3(n-1,h,f,t)



