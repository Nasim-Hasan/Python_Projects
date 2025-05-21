from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing.
    """
    # Since we are placing a known number of beepers, we can use a for-loop to repeat put_beeper()
    for i in range(10):
        put_beeper()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()