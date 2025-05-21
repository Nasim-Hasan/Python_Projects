from karel.stanfordkarel import *

def main():
    """
    Karel will move and put a beeper down if there isn't a wall; Karel will just put a beeper down if there is.
    """
    if front_is_clear():  # If Karel isn't blocked by a wall, move and then put a beeper down
        move()
        put_beeper()
    else:  # If Karel is blocked by a wall, put a beeper down where Karel is currently at
        put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()