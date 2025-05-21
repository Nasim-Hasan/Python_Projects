from karel.stanfordkarel import *

def main():
    """ Places 4 beepers in a row, starting with the position Karel is currently on. """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()