from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(0, 5):
        canvas.create_oval(i*20, i*20, i*20+20, i*20+20)
    

if __name__ == '__main__':
    main()