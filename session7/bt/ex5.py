from turtle import * 

def draw_star(a, b, length):
    penup ()
    goto (a, b)
    pendown()
    for _ in range (5):
        forward (length)
        left (144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


mainloop ()