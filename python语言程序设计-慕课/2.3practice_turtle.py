# -*- coding:utf-8 -*-
# __author__ = 'GuanFengyu'

import turtle
import time
# 1. 绘制等边三角形
turtle.fillcolor("red")
turtle.hideturtle()
turtle.begin_fill()
turtle.penup()
turtle.goto(-200,-50)
turtle.seth(-60)
turtle.pd()
turtle.circle(60, steps=3)
turtle.end_fill()


turtle.penup()
turtle.goto(100,-50)
turtle.begin_fill()
turtle.pd()
turtle.seth(-45)
turtle.circle(90, steps=4)
turtle.end_fill()



time.sleep(5)

# 2. 绘制花瓣










