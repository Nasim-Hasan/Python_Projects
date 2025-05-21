from karel.stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    fill_slot()  # Fencepost problem! This initial fill_slot() prior to the for-loop fixes it.
    for i in range(2):
        move()
        fill_slot()

def fill_slot():
    """ Precondition: Karel is facing East above an empty slot, postcondition: Karel facing East above the same slot, which now has a beeper in it """
    turn_right() # Face South
    move()  # Move inside the slot
    put_beeper()
    turn_around() # Face North
    move()  # Move above the slot
    turn_right()  # Face East

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()