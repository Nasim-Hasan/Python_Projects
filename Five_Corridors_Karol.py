from karel.stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    do_corridor()  # Fencepost problem! This initial do_corridor() fixes it.
    for i in range(4):  # We know we have exactly 4 more corridors to traverse, so we use a for-loop
        turn_left()  # Face North
        move()  # Move up a row
        turn_right()  # Face East
        do_corridor()  # Traverse the next row's corridor

def do_corridor():
    # Precondition: Karel is facing East in column 1; postcondition: Karel is facing East in col 1, corridor has beeper at the end of it.
    move_to_wall()  # Move to the end of the corridor
    if no_beepers_present():  # Put down a beeper if there isn't one already
        put_beeper()
    turn_around()  # Face West
    move_to_wall()  # Return to column 1
    turn_around()  # Face East

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
