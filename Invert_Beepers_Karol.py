from karel.stanfordkarel import *

def main():
    """
    Inverts the pattern of beepers in a single row world.
    """
    invert_corner()  # Fencepost problem! This initial invert_corner() fixes it
    while front_is_clear():  # Since we don't know how many squares we need to invert, use a while-loop
        move()
        invert_corner()  # Invert each corner as we move

def invert_corner():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()