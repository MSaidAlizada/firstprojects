#Importing modules
import time
import turtle
import random
#getting amount of sides
while True:
    side=int(input('Sides:'))
    if side >= 3:
        break
    else:
        print('Please enter a number above 2')
#line color
colors=[]        
for i in range(side):
    color = input('Enter side color:')
    colors.append(color)
#bg color
background = input('What color do you want the background to be?')
#inside color
inside = input('What color do you want the inside to be?')
#getting angle
angle = 360/side
#setting up turtle
t = turtle.Turtle()
t.fillcolor(inside)
turtle.Screen().bgcolor(background)
print('Starting....')
time.sleep(3)
t.begin_fill()
#drawing
for i in range(side):
    t.color(random.choice(colors))
    t.forward(50)
    t.right(angle)
    time.sleep(0.5)
t.fillcolor(inside)    
t.end_fill()
