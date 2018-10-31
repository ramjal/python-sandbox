import turtle

trtl = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


lenght = 20

draw(trtl, lenght, 6)

# draw(trtl, lenght, 6)
# trtl.left(60)
# draw(trtl, lenght, 6)
# trtl.right(120)
# draw(trtl, lenght, 6)
# trtl.left(60)
# draw(trtl, lenght, 6)


trtl.screen.mainloop()