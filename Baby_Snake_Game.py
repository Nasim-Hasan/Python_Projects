from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
left_x_red=360
top_y_red=360
# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #Player(Blue Square)
    left_x_blue=0
    top_y_blue=0
    blue_rectangle=canvas.create_rectangle(left_x_blue,top_y_blue,
    left_x_blue+SIZE,top_y_blue+SIZE,'blue')
    #Goal(Red Square)
    red_rectangle=canvas.create_rectangle(left_x_red,top_y_red,
    left_x_red+SIZE,top_y_red+SIZE,'red')
    animation(canvas,blue_rectangle,left_x_blue,top_y_blue)

def animation(canvas,blue_rectangle,left_x_blue,top_y_blue):
   determiner=0
   while True:
        #..For Direction...
        key=canvas.get_last_key_press()
        if key=='ArrowLeft':
            left_x_blue-=SIZE
            determiner=1
            print('Left Arrow Pressed!')
        elif key=='ArrowRight':
            left_x_blue+=SIZE
            determiner=2
            print('Right Arrow Pressed!')
        elif key=='ArrowUp':
            top_y_blue-=SIZE
            determiner=3
            print('Up Arrow Pressed!')
        elif key=='ArrowDown':
            top_y_blue+=SIZE
            determiner=4
            print('Down Arrow Pressed!')
        #..For Moving...
        if determiner==0:
            left_x_blue+=SIZE
            canvas.moveto(blue_rectangle,left_x_blue,top_y_blue)
            if left_x_blue>CANVAS_WIDTH:
                print('Game Over!')
                break
            if left_x_blue==top_y_red and (top_y_blue+SIZE)==(top_y_red+SIZE):
                print('You Won!')
                break
        elif determiner==1:
            canvas.moveto(blue_rectangle,left_x_blue,top_y_blue)
            left_x_blue-=SIZE
            if left_x_blue<0:
                print('Game Over!')
                break
            if left_x_blue==top_y_red and (top_y_blue+SIZE)==(top_y_red+SIZE):
                print('You Won!')
                break
        elif determiner==2:
            canvas.moveto(blue_rectangle,left_x_blue,top_y_blue)
            left_x_blue+=SIZE
            if left_x_blue>CANVAS_WIDTH:
                print('Game Over!')
                break
            if left_x_blue==top_y_red and (top_y_blue+SIZE)==(top_y_red+SIZE):
                print('You Won!')
                break
        elif determiner==3:
            canvas.moveto(blue_rectangle,left_x_blue,top_y_blue)
            top_y_blue-=SIZE
            if top_y_blue<0:
                print('Game Over!')
                break
            if left_x_blue==top_y_red and (top_y_blue+SIZE)==(top_y_red+SIZE):
                print('You Won!')
                break
        elif determiner==4:
            canvas.moveto(blue_rectangle,left_x_blue,top_y_blue)
            top_y_blue+=SIZE
            if top_y_blue>CANVAS_HEIGHT:
                print('Game Over!')
                break
            if left_x_blue==top_y_red and (top_y_blue+SIZE)==(top_y_red+SIZE):
                print('You Won!')
                break
        time.sleep(DELAY)

if __name__ == '__main__':
    main()