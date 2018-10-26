"""
    Print Letters 
"""
import turtle
import math
from Polygon import circle, arc

trtl = turtle.Turtle()

# Constant height and width of a letter
H = 50
W = 25

# Keep turtle positions
X = 0
Y = 0 

# Move the turtle ahead back to left
def move2FirstPosition(t):
    t.penup()
    t.backward(t.screen.window_width() / 2 - W)
    t.pendown() 

# Move the turtle ahead for the next letter
def move_ahead(t):
    t.penup()
    t.setheading(0)
    t.forward(W * 3)
    t.pendown() 

# forward backward, ending at the original position
def fdbk(t, l):
    t.fd(l)
    t.bk(l)    

# draw letter A
def draw_a(t):
    (X,Y) = t.position()
    t.goto(X + W/2, Y + H)
    angle = t.towards(X+ W, Y + 0)
    t.left(angle)
    t.fd(H/2)
    t.left(180-angle)
    fdbk(t, W/2)
    t.goto(X + W, Y + 0)

# draw letter B
def draw_b(t):
    t.fd(5)
    arc(t, H/4, 180)
    fdbk(t, 5)
    t.left(180)
    arc(t, H/4, 180)
    t.fd(6)
    t.left(90)
    t.fd(H)

# draw letter E
def draw_e(t):    
    (X,Y) = t.position()
    fdbk(t, W)
    t.goto(X, Y + H/2)
    fdbk(t, W)
    t.goto(X, Y + H)
    fdbk(t, W)
    t.goto(X, Y)

########################################

move2FirstPosition(trtl)

draw_a(trtl)

move_ahead(trtl)

draw_b(trtl)

move_ahead(trtl)

draw_e(trtl)

# tells the window to wait for the user to do something
trtl.screen.mainloop()


