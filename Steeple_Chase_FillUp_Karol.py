from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def main():
    put_beeper()
    front_traverse()
    double_left()
    back_traverse()
    turn_right()

def front_traverse():
    while front_is_clear():
        move()
        put_beeper()

def back_traverse():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()
    if front_is_blocked():
        for i in range(3):
            turn_left()
        while front_is_clear():
            move()
    else:
        move()
        for i in range(3):
            turn_left()
        main()
    
def double_left():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()