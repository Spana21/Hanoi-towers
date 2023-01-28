from Projekt.Models.Vykresleni import *
import time

def move_disc(disc, pin):
    while disc.ycor() < 100:
        disc.goto(disc.xcor(), disc.ycor() + 5)
        win.update()
    disc.goto(pin.xcor(), 100)
    win.update()
    while disc.ycor() > pin.pos_list[pin.count]:
        disc.goto(disc.xcor(), disc.ycor() - 5)
        win.update()
    time.sleep(0.001)  # adjust speed



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
    elif f == 'D':
        top_disc = s4.discs[-1]
        start_pin = s4

    if t == 'A':
        s = s1
    elif t == 'B':
        s = s2
    elif t == 'C':
        s = s3
    elif t == 'D':
        s = s4

    move_disc(top_disc, s)
    start_pin.count -= 1
    start_pin.discs.pop()
    s.count += 1
    s.discs.append(top_disc)

# n number of discs
# f from position, h and k helper(via), t target
def hanoi4(n, f, h,k,t):
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
    if n == 1:
        move(f,t)
        return
    hanoi3(n-1,f,t,h)
    move(f,t)
    hanoi3(n-1,h,f,t)