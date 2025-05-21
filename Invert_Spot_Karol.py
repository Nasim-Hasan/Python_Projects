from karel.stanfordkarel import *

def main():
    """
    Inverts the spot Karel is currently standing on.
    """
    # If Karel detects a beeper, we want to "invert" the spot and pick it up so there is no beeper
    if beepers_present():
        pick_beeper()

    # If Karel doesn't detect a beeper, we want to "invert" the spot and place a beeper so there is one
    else:
        put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()