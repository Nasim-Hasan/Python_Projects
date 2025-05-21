from karel.stanfordkarel import *

def main():
    """
    Fills entire bottom row of any sized world with beepers.
    """
    # Fencepost problem! We need to put a beeper here or else we will move without placing a beeper on the first square.
    put_beeper()
  
    # We don't know how large the world is, so we can use a while-loop to move until we reach the last column
    while front_is_clear():
        move()
        put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()