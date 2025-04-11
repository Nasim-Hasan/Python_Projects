"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
     if left_is_clear():
            put_beeper()
            move()
            turn_left()
            move()
            put_beeper()
     upper_row_fill()

def upper_row_fill():
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()
            main()
        else:
            turn_right()
            move()
            turn_left()
        
def turn_right():
     for i in range (3):
          turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()