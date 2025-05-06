from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    bricks_in_base=BRICKS_IN_BASE
    prv_top_y=0
    while bricks_in_base!=0:
        left_x=CANVAS_WIDTH/bricks_in_base
        if bricks_in_base<BRICKS_IN_BASE:
            top_y=CANVAS_HEIGHT-(prv_top_y+BRICK_HEIGHT)
            bottom_y=BRICK_HEIGHT
        else:
            top_y=CANVAS_HEIGHT-BRICK_HEIGHT
            bottom_y=CANVAS_HEIGHT
        for i in range(bricks_in_base):
            right_x=left_x+BRICK_WIDTH
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                'yellow',
                'black'
            )
            left_x=right_x
        bricks_in_base-=1
        prv_top_y=top_y

if __name__ == '__main__':
    main()