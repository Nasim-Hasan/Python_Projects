from karel.stanfordkarel import *

def main():
    """ Turns Karel until facing a wall. """
    # We don't know exactly what direction Karel is facing nor which side a wall will be on!
    while front_is_clear():  # We can use a while-loop to turn until the front isn't clear (we find a wall)!
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()