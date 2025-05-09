from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
DOOR_WIDTH = CANVAS_WIDTH * 0.25  # Each door takes up 1/4 of of the canvas's width
DOOR_HEIGHT = CANVAS_HEIGHT * 0.4 # Each door takes up 2/5 of the canvas's height
DOOR_GAP = (CANVAS_WIDTH - (3 * DOOR_WIDTH)) // 4

def get_door_clicked(canvas):
    """
    Returns the door that was clicked. If no door was clicked, return None.
    
    Hint: You may find the find_overlapping(...) function to be useful here!
    """
    x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
    overlapping = canvas.find_overlapping(x, y, x, y)
    if len(overlapping) > 0:  # Checks to see if there are any overlapping shapes
        return overlapping[0]
    
    return None


################### No need to edit code beyond this point :) ###################

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    door_1 = make_door(canvas, DOOR_GAP, "1", color="red")
    door_2 = make_door(canvas, DOOR_WIDTH + 2 * DOOR_GAP, "2", color="blue")
    door_3 = make_door(canvas, DOOR_WIDTH * 2 + 3 * DOOR_GAP, "3", color="yellow")
    
    while True:
        click = canvas.get_last_click()
        if click:
            door_clicked = get_door_clicked(canvas)
            
            if door_clicked:
                open_door(canvas, canvas.get_left_x(door_clicked))

def make_door(canvas, left_x, door_number, color="black"):
    """
    Makes a door starting at the specified left_x. Dimensions of the door vary
    based on the canvas's dimensions. Also creates text above the door with the
    specified door_number.
    """
    
    door = canvas.create_rectangle(left_x,
                                   CANVAS_HEIGHT - DOOR_HEIGHT,
                                   left_x + DOOR_WIDTH,
                                   CANVAS_HEIGHT,
                                   color=color)
    
    font_size = 24
    door_text = canvas.create_text(left_x + DOOR_WIDTH/2 - font_size/4, 
                                   CANVAS_HEIGHT - DOOR_HEIGHT - font_size,
                                   text=str(door_number),
                                   font_size=font_size)
    
    return door

def open_door(canvas, left_x):
    """
    "Opens" a door by creating a white rectangle within a door. This function
    assumes that the left_x provided is the same left_x which is used to make
    one of the three doors.
    """
    
    door_frame_size = DOOR_WIDTH * 0.15
    canvas.create_rectangle(left_x + door_frame_size,
                            CANVAS_HEIGHT - DOOR_HEIGHT + door_frame_size,
                            left_x + DOOR_WIDTH - door_frame_size,
                            CANVAS_HEIGHT,
                            color="white")


if __name__ == '__main__':
    main()