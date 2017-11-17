import turtle
import time

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.pencolor("pink")
        turtle.circle(-rad,angle)
        turtle.pencolor("yellow")
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("red")
    for i in range(6):
        turtle.seth(60*i)
        drawSnake(40,80,3,pythonsize/2)
        turtle.penup()
        turtle.home()
        turtle.pendown()
    time.sleep(5)

main()

