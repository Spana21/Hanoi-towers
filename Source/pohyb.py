# import the Veze module from the Source package
from Source.VezeADisky import *
import time

# move_disc function to move disc from start to end
def move_disc(disc, pin):
    while disc.ycor() < 100:
        disc.goto(disc.xcor(), disc.ycor() + 5)
        win.update()
    disc.goto(pin.xcor(), 100)
    win.update()
    while disc.ycor() > pin.pos_list[pin.count]:
        disc.goto(disc.xcor(), disc.ycor() - 5)
        win.update()
    time.sleep(0.01)  # adjust speed

# move function to move top disc from start pin to end pin
def move(f, t):
    print(f'Move disc from {f} to {t}!')
    if f == 'A':
        top_disc = s1.discs[-1]
        start_pin = s1
    elif f == 'B':
        top_disc = s2.discs[-1]
        start_pin = s2
    elif f == 'C':
        top_disc = s3.discs[-1]
        start_pin = s3

    if t == 'A':
        s = s1
    elif t == 'B':
        s = s2
    elif t == 'C':
        s = s3

    move_disc(top_disc, s)
    start_pin.count -= 1
    start_pin.discs.pop()
    s.count += 1
    s.discs.append(top_disc)

# n number of discs
# f from position, h helper(via) and target
def hanoi(n, f, h, t):
    if n == 0:  # Prevent from moving 0 or negative discs
        pass
    else:
        hanoi(n - 1, f, t, h)  # move all but bottom to helper (A to B using C)
        move(f, t)  # move bottom disc to target (from A to C)
        hanoi(n - 1, h, f, t)  # move rest from helper to target via from (from B to C using A)

