"""
This is a worked example. Karel will "invert" each beeper 
in the first row. To invert a beeper: if there was a beeper
pick it up. Otherwise, put one down.
"""
from karel.stanfordkarel import *

def main():
    # invert beeper on each corner in the row
    while front_is_clear():
        invert_beeper()
        move()
    # fence-post bug correction
    invert_beeper()
    if front_is_blocked():
        turn_left()
        turn_left()
        while front_is_clear():
            move()
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range (3):
        turn_left()


def invert_beeper():
    """ flips whether or not there is a beeper """
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()