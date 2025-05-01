from graphics import Canvas

CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# the diameter of the outer red circle
OUTER_DIAMETER = 50

# the left and top co-ordinates of the outer red circle
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER)/2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER)/2
OUTER_RIGHT_X = OUTER_LEFT_X + OUTER_DIAMETER
OUTER_BOTTOM_Y = OUTER_TOP_Y + OUTER_DIAMETER

# the size of the red band of the ring
RING_WIDTH = 10

# the diameter of the inner white circle
INNER_DIAMETER = (OUTER_DIAMETER - RING_WIDTH)/2

# the left and top co-ordinates of the inner white circle
INNER_LEFT_X = OUTER_LEFT_X + RING_WIDTH
INNER_TOP_Y = OUTER_TOP_Y + RING_WIDTH
INNER_RIGHT_X = INNER_LEFT_X + 1.5*INNER_DIAMETER
INNER_BOTTOM_Y = INNER_TOP_Y + 1.5*INNER_DIAMETER

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_oval(OUTER_LEFT_X, OUTER_TOP_Y, OUTER_RIGHT_X, OUTER_BOTTOM_Y, "red")
    canvas.create_oval(INNER_LEFT_X, INNER_TOP_Y, INNER_RIGHT_X, INNER_BOTTOM_Y, "white")
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
    