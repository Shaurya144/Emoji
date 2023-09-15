from turtle import *
import time

for i in range(8):
    circle(100, 45)

penup()
goto(-30, 50)
time.sleep(1)

pendown()
pencolor("green")
pensize(3)
for i in range(2):
    fd(25)
    lt(90)
    fd(75)
    lt(90)


penup()
goto(30, 50)
time.sleep(1)

pendown()
pencolor("green")
pensize(3)
for i in range(2):
    fd(25)
    lt(90)
    fd(75)
    lt(90)

penup()
goto(-10, 20)
time.sleep(1)

pendown()
pensize(4)
pencolor("red")

fd(40)
lt(45)
fd(20)
rt(90)
fd(10)
rt(90)
fd(20)
rt(45)
fd(40)
fd(40)
rt(45)
fd(20)
rt(90)
fd(10)
rt(90)
fd(20)
lt(45)
fd(40)

time.sleep(5)