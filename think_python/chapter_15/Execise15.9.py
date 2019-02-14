import math  
import turtle

class Point:
    """Represents a point.

    attributes: x, y.
    """


class Circle:
    """Represents a circle.
    
    attributes: center, radius.
    """        

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


# draws a polygon
def polygon(t, length, n):
    # more accurate than 360 / n
    # when numerator is float the result will also be float
    angle = 360.0 / n 
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# draws a circle with radius of r
def drawcircle(t, r):
    #t.setpos(r/2, r/2)
    circumference = 2 * math.pi * r
    n = 200 # the larger n the cleaner arc but slower drawing
    length = circumference / n
    polygon(t, length, n)


# Return the distant between two points
def points_distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y    
    return math.sqrt(dx**2 + dy**2)


def point_in_circle(circle, point):
    return points_distance(circle.center, point) < circle.radius


def rect_in_circle(circle, rectangle):
    p0 = Point()
    p1 = Point()
    p2 = Point()
    p3 = Point()

    p0.x = rectangle.corner.x
    p0.y = rectangle.corner.y
    p1.x = rectangle.corner.x + rectangle.width
    p1.y = rectangle.corner.y
    p2.x = rectangle.corner.x
    p2.y = rectangle.corner.y + rectangle.height
    p3.x = rectangle.corner.x + rectangle.width
    p3.y = rectangle.corner.y
    p3.x = rectangle.corner.x
    p3.y = rectangle.corner.y + rectangle.height

    return points_distance(circle.center, p0) < circle.radius \
        and points_distance(circle.center, p1) < circle.radius \
        and points_distance(circle.center, p2) < circle.radius \
        and points_distance(circle.center, p3) < circle.radius


def draw_rect(bob, rect):
    bob.penup()
    bob.setpos(rect.corner.x, rect.corner.y)
    bob.pendown()
    bob.forward(rect.width)
    bob.right(-90)
    bob.forward(rect.height)
    bob.right(-90)
    bob.forward(rect.width)
    bob.right(-90)
    bob.forward(rect.height)
    bob.right(-90)
    
def draw_circle(bob, circle):
    bob.penup()
    bob.setpos(circle.center.x, c.center.y-circle.radius)
    bob.pendown()
    drawcircle(bob, circle.radius)

#testing now
c = Circle()
c.center = Point()
c.center.x = 100
c.center.y = 60
c.radius = 50

p = Point()
p.x = 155
p.y = 105
print('Point in circle: ' + str(point_in_circle(c, p)))

r = Rectangle()
r.width = 50
r.height = 30
r.corner = Point()
r.corner.x = 62
r.corner.y = 30

#rect_in_circle(c, r)
print('Rect in circle: ' + str(rect_in_circle(c, r)))

bob = turtle.Turtle()

bob.forward(200)
bob.backward(200)
bob.right(-90)
bob.forward(200)
bob.backward(200)
bob.right(90)

print(r.corner.x)
print(r.corner.y)

draw_rect(bob, r)
draw_circle(bob, c)

turtle.Screen().mainloop()
