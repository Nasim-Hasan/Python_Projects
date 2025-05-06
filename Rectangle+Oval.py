from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(100,0,300,200)
    canvas.create_oval(150,200,250,400,'red')

if __name__ == '__main__':
    main()