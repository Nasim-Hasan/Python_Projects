"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create mirror line
    canvas.create_line(
        CANVAS_WIDTH // 2, 
        0, 
        CANVAS_WIDTH // 2, 
        CANVAS_HEIGHT)
    
    # Create red rectangle
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x, 
        rect_top_y, 
        rect_left_x + rect_width, 
        rect_top_y + rect_height, 
        'red')
    
    # Create blue rectangle
    canvas.create_rectangle(
        CANVAS_WIDTH - rect_left_x - rect_width,  # Start at right bound, move left rect_left_x, move left rect_width
        rect_top_y,  # Same top_y as red rectangle
        CANVAS_WIDTH - rect_left_x,  # Take our left_x from two lines above and add our rect_width to it
        rect_top_y + rect_height,  # Same bottom_y as red rectangle
        'blue')
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()