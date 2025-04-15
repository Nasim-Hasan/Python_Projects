from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""
def main():
    turn_left()
    move()
    turn_right()
    move()
    if front_is_clear():
        move()
        turn_right()
        move()
        put_beeper()
        turn_left()
    else:
        turn_around()
        move()
        turn_left()
        move()
        put_beeper()
        turn_left()

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range (3):
        turn_left()

if __name__ == '__main__':
    main()