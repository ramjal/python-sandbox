import turtle
import math

bob = turtle.Turtle()

# draws a sqare
def square(t, length):    
    for i in range(4):
        t.fd(length)
        t.lt(90)

# draws a polygon
def polygon(t, length, n):
    # more accurate than 360 / n
    # when numerator is float the result will also be float
    angle = 360.0 / n 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# draws a circle with radius of r
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 200 # the larger n the cleaner arc but slower drawing
    length = circumference / n
    polygon(t, length, n)

# draws an arc with radius of r
def arc(t, r, angle):
    n = 200 # the larger n the cleaner arc
    length = (angle / 360) * (2 * math.pi * r) / n
    for i in range(n):
        t.fd(length)
        t.lt(angle / n) 

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

# tells the window to wait for the user to do something
turtle.mainloop()



