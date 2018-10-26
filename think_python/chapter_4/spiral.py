# print Archimedian spiral
from Polygon import circle, arc
import turtle

trtl = turtle.Turtle()

def print_spiral1(t):
    l = 1
    while l < 400:
        arc(t, l, 60)
        if l < 10:
            l += 2
        elif l < 20:
            l += 5
        else:
            l += 10


def print_spiral2(t, cte):
    l = 1
    while l < 400:
        arc(t, l, 60)
        l *= cte


print_spiral1(trtl)

trtl.penup()
trtl.home()
trtl.pendown()

print_spiral2(trtl, 1.2)

trtl.screen.mainloop()