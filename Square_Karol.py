from karel.stanfordkarel import *

def main():
    """
    Makes Karel place beepers in a square (4 beepers total) and end in the same position Karel starts in.
    """
    # If we consider the task carefully, we need to repeat several actions
    # Since we are repeating a these actions a known number of times, we use a for-loop
    for i in range(4):
        # Put beeper
        put_beeper()

        # Makes us move in a square motion when we do it four times
        move()
        turn_left()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()