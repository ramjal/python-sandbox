# import the math module  
import math  

# class Point
class Point:
    x = 3.0
    y = 4.0

# Print point coordinates
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

# Return the distant between two points
def points_distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y    
    return math.sqrt(dx**2 + dy**2)

    
p1 = Point()
p2 = Point()

p1.x = 3
p1.y = 3

p2.x = 6
p2.y = 7

print_point(p1)
print_point(p2)
dis = points_distance(p1, p2)

print('Distance between (%g, %g) and (%g, %g): %g' % (p1.x, p1.y, p2.x, p2.y, dis))
