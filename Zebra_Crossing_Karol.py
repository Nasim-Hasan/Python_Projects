"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    draw_stripe()
    while front_is_clear():
        for i in range (4):
             move()
        draw_stripe()

def draw_stripe():
    turn_left()
    beeper_column()
    turn_right()
    move()
    turn_right()
    beeper_column()
    turn_left()

def beeper_column():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()