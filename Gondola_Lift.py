from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
DELAY = 0.01
NUM_STEPS = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    lift_left_x = 0
    lift_bottom_y = CANVAS_HEIGHT - 50
    
    # note these helpful variables!
    lift_width = CANVAS_WIDTH
    lift_height = lift_bottom_y
    
    canvas.create_line(
        lift_left_x, lift_bottom_y,
        lift_left_x + lift_width, lift_bottom_y - lift_height)

    gondola = canvas.create_rectangle(
        0, lift_bottom_y, 
        SQUARE_SIZE, lift_bottom_y + SQUARE_SIZE)

    for step_num in range(NUM_STEPS):
	    # write your code here!
        lift_left_x+=step_num*(lift_width/NUM_STEPS)
        lift_bottom_y-=step_num*(lift_height/NUM_STEPS)
        canvas.moveto(gondola,lift_left_x,lift_bottom_y)
        time.sleep(DELAY)

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()