from karel.stanfordkarel import *

def main():
    make_diagonal()
    traverse_down()

def traverse_down():
    turn_right()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()

def turn_around():
    for i in range (2):
        turn_left()
    move()
    turn_left()
    move()
    reverse_diagonal()

def reverse_diagonal():
    # keep stepping up until the top
    while front_is_clear():
        # Assume: Karel is facing right (east) 
        put_beeper()
        turn_right()
        move()
        turn_left()
        move()
    put_beeper()
  
def make_diagonal():
    # keep stepping up until the top
    while front_is_clear():
        # Assume: Karel is facing right (east) 
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
    put_beeper()
    
def turn_right():
    # defines turn_right as 3x turn_left
    for i in range(3):
        turn_left()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()