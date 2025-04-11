"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
from karel.stanfordkarel import *

def main():
    # Karel makes springtime happen by blooming both flower stems in the world!
    for i in range(2):  # We know there will be exactly two stems, so we can use a for-loop to bloom them!
        move_to_wall()  # Move to the next stem
        bloom_flower()
    move_to_wall()  # Fencepost problem! This fixes it. :)

def bloom_flower():
    """
    Karel places a bloom on top of the stem she is facing.

    Pre: Karel is on row 1 to the immediate left of a stem facing East.
    Post: Karel is on row 1 to the immediate right of a stem facing East.
    """
    climb_stem()
    make_bloom()
    move_to_wall()
    turn_left()

def climb_stem():
    """
    Karel climbs the stem until the top, at the bottom left corner of where the bloom will go.

    Pre: Karel is at the base of the stem facing East.
    Post: Karel is at the bottom left corner of the bloom facing North.
    """
    turn_left()
    while right_is_blocked():
        move()

def make_bloom():
    """
    Karel makes the flower bloom with beepers!

    Pre: Karel is on the bottom left corner of the bloom facing North
    Post: Karel is on the bottom right corner of the bloom facing South
    """
    # Makes a square of beepers
    put_beeper()
    move()
    for i in range(2):
        put_beeper()
        turn_right()
        move()
    put_beeper()

def move_to_wall():
    # Karel moves until blocked.
    while front_is_clear():
        move()

def turn_right():
    for i in range (3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()