from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    left_x = 0
    top_y = 0
    right_x = left_x + CANVAS_WIDTH
    bottom_y = top_y + CANVAS_HEIGHT/2

    canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        'red'
    )
    
if __name__ == '__main__':
    main()