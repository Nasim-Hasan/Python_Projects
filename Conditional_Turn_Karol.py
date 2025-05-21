
from karel.stanfordkarel import *

def main():
    """ 
    Turns left if there is a beeper present; turns right if  there are no beepers present. 
    """
    if beepers_present():  # Only when Karel detects a beeper do we turn left
        turn_left()
    else:  # If no beepers are detected, turn right
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()