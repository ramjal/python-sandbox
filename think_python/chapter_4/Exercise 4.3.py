import turtle
bob = turtle.Turtle()
# print(bob)

def square(t, length):    
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        
square(bob, 100)

bob.penup()
bob.backward(200)
bob.pendown()

polygon(bob, 80, 8)

bob.screen.mainloop()



