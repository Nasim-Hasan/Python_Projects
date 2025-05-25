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
    for row in range(BRICKS_IN_BASE):
        bricks_in_row=BRICKS_IN_BASE-row
        y_top=CANVAS_HEIGHT-(row+1)*BRICK_HEIGHT
        start_x=(CANVAS_WIDTH-bricks_in_row*BRICK_WIDTH)/2
        for brick in range(bricks_in_row):
            left_x=start_x+brick*BRICK_WIDTH
            top_y=y_top
            right_x=left_x+BRICK_WIDTH
            bottom_y=top_y+BRICK_HEIGHT
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                'yellow',
                'black'
            )

if __name__ == '__main__':
    main()