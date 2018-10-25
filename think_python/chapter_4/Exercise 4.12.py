import turtle
import math

bob = turtle.Turtle()

# draws a poliyline
def polyline(t, step_length, n, step_angle):
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# draws a sqare
def square(t, length):    
    polyline(t, length, 4, 90)

# draws a polygon
def polygon(t, length, n):
    # more accurate than 360 / n
    # when numerator is float the result will also be float
    angle = 360.0 / n 
    polyline(t, length, n, angle)

# draws a circle with radius of r
def circle(t, r):
    arc(t, r, 360)

# draws an arc with radius of r
def arc(t, r, angle):
    n = 100 # the larger n the cleaner arc
    arc_length = 2 * math.pi * r * angle / 360
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, step_length, n, step_angle)


def test(rep, radius):
    angle = 360 / rep
    for i in range(rep):
        for j in range(2):
            arc(bob, radius, angle)
            bob.lt(180 - angle)
        bob.lt(angle)
    
bob.penup()
bob.backward(300)
bob.pendown()

test(7, 100)

bob.penup()
bob.forward(300)
bob.pendown()

test(20, 200)

    
"""
bob.penup()
bob.forward(300)
bob.pendown()
        
square(bob, 100) # or we can do: square(bob, length=100)

bob.penup()
bob.backward(200)
bob.pendown()

polygon(bob, 50, 8)

bob.penup()
bob.backward(200)
bob.pendown()

circle(bob, 80)

bob.penup()
bob.backward(200)
bob.pendown()
   
arc(bob, 80, 270)
"""

# tells the window to wait for the user to do something
# turtle.mainloop()



