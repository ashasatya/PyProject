
from turtle import *
from random import randint
import time

#  Speed the turtle module to draw faster from co-ordinates at (-140,140)
speed(10)
penup()
goto(-140, 140)
# Draw the vertical lines to create a track
for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
#   add first turtle with color red & shape
ada = Turtle()
ada.color('red')
ada.shape('turtle')
#   add the starting coordinates for the first turtle (-160, 100)
ada.penup()
ada.goto(-160, 100)
ada.pendown()
#   add second turtle with color blue & shape
bob = Turtle()
bob.color('blue')
bob.shape('turtle')
#   add the starting coordinates for the second turtle (-160, 70)
bob.penup()
bob.goto(-160, 70)
bob.pendown()
#   add third turtle with color orange & shape
joe = Turtle()
joe.color('orange')
joe.shape('turtle')
#   add the starting coordinates for the third turtle (-160, 40)
joe.penup()
joe.goto(-160, 40)
joe.pendown()
#   add fourth turtle with color purple & shape
zoe = Turtle()
zoe.color('purple')
zoe.shape('turtle')
#   add the starting coordinates for the fourth turtle (-160, 10)
zoe.penup()
zoe.goto(-160, 10)
zoe.pendown()

#   Generate the random steps for each turtle
for turn in range(100):
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    joe.forward(randint(1, 5))
    zoe.forward(randint(1, 5))

time.sleep(5)