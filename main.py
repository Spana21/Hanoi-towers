from ClassDisky import *
from Sloupce import *
import argparse
"""
This code implements the solution to the Towers of Hanoi puzzle with a graphical representation using the Turtle library.
The script can be run from the command line, with the number of disks, number of columns, and the destination column specified as command-line arguments. The `ArgumentParser` module is used to parse these arguments and pass them to the `main` function.

"""

def main(number,sloupce,kam):
    """
       This function sets up the turtle graphics window, initializes the base, and draws the disks and columns for the Towers of Hanoi puzzle.

       Args:
           number (int): The number of disks to be used in the puzzle.
           sloupce (int): The number of columns to be used in the puzzle (3 or 4).
           kam (int): The column to which the disks will be sorted.

       Returns:
           None
       """

    target = kam

    # Create a turtle graphics window
    win = turtle.Screen()
    run_turtle(win)

    # Initialize the base
    base()

    # Draw the disks
    Disky(number)

    # Draw the columns
    if sloupce == 3:
        Sloupce3(target,number)

    if sloupce == 4:
        Sloupce4(target,number)

    # Keep the turtle graphics window open after the animation
    turtle.done()

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Parametry hlavolamu')
    parser.add_argument("disky", metavar="disky", type=int, help = "Pocet disku")
    parser.add_argument("sloupce", metavar="sloupce", type=int, help="Pocet sloupcu (3 nebo 4)")
    parser.add_argument("kam", metavar="kam", type=int, help="Na jaky sloupec se budou disky radit")
    arguments = parser.parse_args()
    main(arguments.disky, arguments.sloupce, arguments.kam)


