from karel.stanfordkarel import *

def main():
    """ Moves Karel forward until a wall. """
    while front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()