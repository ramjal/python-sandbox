import turtle
import math

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
