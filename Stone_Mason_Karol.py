from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
def main():
  turn_left()
  while front_is_clear():
     build_column()
  put_beeper()
  turn_right()
  if front_is_clear():
    move()
    turn_right()
    for i in range (4):
        move()
    turn_left()
    distance_traverse()
  else:
     turn_right()
     for i in range (4):
        move()
     turn_left()

def build_column():
   put_beeper()
   move()

def turn_right():
    for i in range (3):
        turn_left()

def distance_traverse():
    for i in range (3):
        move()
    main()

if __name__ == '__main__':
    main()