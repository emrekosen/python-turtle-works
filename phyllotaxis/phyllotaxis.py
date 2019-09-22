import turtle
import math
import colorsys

# bigger number will be bigger circle
loop_number = 2000

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

feride = turtle.Turtle()
feride.penup()
feride.speed(20)
feride.pensize(0.5)

for n in range(loop_number):
    # angle
    # you can change angle to 137.3 or 137.6 to draw different phyylotaxis
    a = n * 137.5
    a_radian = math.radians(a)
    # radius of dot
    r = 5 * math.sqrt(n)
    # X coordinate
    xcoor = r * math.cos(a_radian)
    # Y coordinate
    ycoor = r * math.sin(a_radian)
    # pen color -- converts hsv to rgb
    feride.pencolor(tuple(round(i*255) for i in colorsys.hsv_to_rgb((2*a % 256)/255, 1, 1)))
    feride.setpos(xcoor, ycoor)
    feride.dot()
      
turtle.done() 
