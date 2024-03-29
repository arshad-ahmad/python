from turtle import *
from random import randint
from colorsys import hsv_to_rgb

step = 50
nsteps = 2000
hinc = 3.0/nsteps
width(2)

(w,h)= screensize()
speed(2)
colormode(1.0)
bgcolor('black')
hue=0.0
for i in range(nsteps):
    setheading(randint(0,359))
    color(hsv_to_rgb(hue, 0.0,1.0))
    hue+=hinc
    forward(step)
    (x,y)=pos()
    if abs(x)>w or abs(y)>h:
        backward(step)
