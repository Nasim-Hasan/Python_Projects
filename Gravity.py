from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = random.random() * CANVAS_WIDTH
    start_y = random.random() * CANVAS_HEIGHT
    square = canvas.create_rectangle(start_x, start_y,
                    start_x + SQUARE_SIZE,
                    start_y + SQUARE_SIZE)

    while (start_y + SQUARE_SIZE)<=CANVAS_HEIGHT:
         start_y+=VELOCITY
         canvas.moveto(square,start_x,start_y)
         time.sleep(DELAY)


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()