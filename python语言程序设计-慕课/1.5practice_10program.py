# 1.5 第一章练习


# 1.字符串拼接

str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家的名字：")
print("世界这么大，{}想去{}看看。".format(str1,str2))

# 补充学习：print format 格式整理


# 2.整数序列求和

n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i+1;
print("1到N的求和结果是：",sum )

# range [ ):左闭右开



# 3. 九九乘法表

for i in range(1,10):
    for j in range(i,10):
        print("{}*{}={:2}".format(i,j,i*j),end=' ')
    print(' ')

# 4. 阶乘计算

sum,temp = 0,1
for i in range(1,11):
    temp *= i;
    sum += temp;
print("1!+2!+...+10!={}".format(sum))
    
# 5. 猴子摘桃，第一天摘了若干桃子，第一天吃了一半+一个桃子，第二天剩下的一半+1，到第五天，只剩一个桃子。

n = 1
for i in range(5,0,-1):
    n = (n+1)<<1
print(n)

# 6. 健康食谱输出。列出5种不同食材，输出他们可能组成的所有菜的名字。

diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y):
            print("{}{}".format(diet[x],diet[y]))


# 7.五角星的绘制

from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()


# 8. 太阳花的绘制

from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()


# 9.螺旋线的绘制

import time
import turtle
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)

# 10.彩色螺旋线的绘制

import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)

