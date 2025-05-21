from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()  # Face North
    move_three_times()  # Move up the arch
    turn_right()  # Face East
    move_three_times()  # Move across the arch
    turn_right()  # Face South
    move_three_times()  # Move down the arch
    turn_left()  # Face East

def move_three_times():
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()