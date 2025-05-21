from karel.stanfordkarel import *

def main():
    """ If Karel is facing a wall, put a beeper, turn left and move forward."""
    if front_is_blocked():  # Karel is facing a wall if their front is blocked!
        put_beeper()
        turn_left()
        move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()