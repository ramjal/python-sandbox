import turtle
import math

trtl = turtle.Turtle()

# draws a poliyline
def polyline(t, step_length, n):
    step_angle = 360/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def polyline2(t, step_length, n):
    step_angle = 360 / n
    inside_angle = (180 - step_angle) / 2
    inside_step = step_length / (2 * (math.sin(math.pi / n)))
    print(inside_step)
    print(math.sin(180 / n))
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        t.lt(inside_angle)
        t.fd(inside_step)
        t.backward(inside_step)
        t.rt(inside_angle)

trtl.penup()
trtl.backward(350)
trtl.pendown()

trtl.lt(10)
polyline2(trtl, 100, 5)

trtl.penup()
trtl.setx(0)
trtl.sety(0)
trtl.pendown()

trtl.lt(20)
polyline2(trtl, 100, 6)

trtl.penup()
trtl.setx(300)
trtl.sety(0)
trtl.pendown()

trtl.lt(10)
polyline2(trtl, 80, 7)
    

## tells the window to wait for the user to do something
trtl.screen.mainloop()






