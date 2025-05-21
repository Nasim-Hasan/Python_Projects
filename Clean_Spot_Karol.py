from karel.stanfordkarel import *

def main():
    """ Picks up beepers in current spot until there are none left."""
    for i in range(5):
        if beepers_present():
            pick_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()