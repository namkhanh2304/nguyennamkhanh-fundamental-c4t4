from turtle import *

def draw_square(x, y):
    speed(-1)
    color(y)
    for i in range(4):
        forward(x)
        left(90)


# minh duc
for i in range(30):
    draw_square(i * 5, 'orange')
    left(17)
    penup()
    forward(i * 2)
    pendown()


mainloop()    