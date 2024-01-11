import turtle
import time
Python_rules=turtle.Screen()
turtle.screensize(1200,1200)
turtle.bgcolor('black')
turtle.shape('turtle')
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
move=1

t2.speed(0)
for i in range(10):
    for i in range(4):
          t2.pu() #penup
          t2.goto(300,250)
          t2.pd() #pendown
          t2.color('cyan')
          t2.pensize(3)
          t2.circle(50,steps=4)# Φτιάξει ένα κύκλο με ακτίνα 50px σε 4 βήματα, δηλ. με 4 ακμές - ένα τετράγωνο
          t2.right(100)#στρίψε δεξιά 100 μοίρες

t3.speed(0)
for i in range(6):
    for i in range(4):
          t3.pu() #penup
          t3.goto(0,0)
          t3.pd() #pendown
          t3.color('light green')
          t3.pensize(3)
          t3.circle(100,steps=6)
          t3.right(100)
          
t4.speed(0)
for i in range (7):
    for i in range (2):
        t4.pensize(5)
        t4.goto(370,0)
        t4.color("green")
        t4.forward(100)
        t4.right(60)
        t4.color("cyan")
        t4.forward(50)
        t4.right(120)
    t4.right(30)
    
t5.speed(0)
for i in range (7):
    for i in range (2):
        t5.pensize(7)
        t5.goto(-370,0)
        t5.color("purple")
        t5.forward(100)
        t5.circle(5,steps=4)
        t5.right(60)
        t5.color("violet")
        t5.forward(50)
        t5.right(120)
    t5.right(30)
