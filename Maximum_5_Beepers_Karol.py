from karel.stanfordkarel import *

def main():
    """
    Karel should place 5 beepers in the bottommost row of the world if the world is more than 5 columns wide.
    If the world is less than 5 columns wide, Karel should fill the bottommmost row with beepers and not walk through any walls.
    """
    put_beeper()  # Fencepost bug! This initial put_beeper fixes it.
    for i in range(4):  # We know we want to place at most 4 more beepers, so use a for-loop.
        if front_is_clear():  # Only move and place a new beeper if there isn't a wall!
            move()
            put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()