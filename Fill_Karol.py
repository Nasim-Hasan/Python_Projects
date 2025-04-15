from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""
def main():
  while front_is_clear():
    put_beeper()
    move()
  put_beeper()
  turn_around()
  traverse_back()

def turn_around():
   turn_left()
   turn_left()

def traverse_back():
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
        main()
    else:
        turn_right()
        while front_is_clear():
            move()

def turn_right():
    for i in range (3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()