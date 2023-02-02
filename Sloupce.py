from Pohyb import *


def Sloupce4(target, number):
    """
       This function implements the Tower of Hanoi for 4 columns.

       Parameters:
       target (int): The number of the column to which the disks will be moved
       number (int): The number of discs in the game.

       Returns:
       None
       """
    if target == 4:
        # Call the hanoi4 function to start the animation where the discs will be moved to the 4th column
        hanoi4(number, 'A', 'B', 'C', 'D')
    elif target == 3:
        # Call the hanoi4 function to start the animation where the discs will be moved to the 3rd column
        hanoi4(number, 'A', 'B', 'D', 'C')
    elif target == 2:
        # Call the hanoi4 function to start the animation where the discs will be moved to the 2nd column
        hanoi4(number, 'A', 'C', 'D', 'B')
    else:
        print("Sloupec neexistje")


def Sloupce3(target, number):
    """
     This function implements the Tower of Hanoi for 3 columns.

     Parameters:
         target (int): The number of the column to which the disks will be moved
         number (int): The number of discs in the game.

     Returns:
         None
     """
    if target == 3:
        # Call the hanoi3 function to start the animation where the discs will be moved to the 3rd column
        hanoi3(number, 'A', 'B', 'C')
    elif target == 2:
        # Call the hanoi3 function to start the animation where the discs will be moved to the 2rd column
        hanoi3(number, 'A', 'C', 'B')
    else:
        print("Sloupec neexistje")
