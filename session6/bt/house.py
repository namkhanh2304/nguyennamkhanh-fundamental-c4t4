from turtle import *
speed(-1)

penup()
backward(100)
left(90)
backward(100)
right(90)
pendown()


for i in range (2):
    forward(200)
    left(90)
    forward(220)
    left(90)
left(90)
forward(220)
color("red")


penup()
begin_fill()
right(45)
forward(200/(2**0.5))
right(90)
forward(200/(2**0.5))
right(135)
end_fill()


forward(50)
left(90)
forward(20)


begin_fill()
for i in range(4):
    forward(40)
    left(90)
color("yellow")
end_fill()


forward(80)
right(90)
forward(80)


begin_fill()
for i in range (2):
    forward(50)
    left(90)
    forward(120)
    left(90)
color("blue")
end_fill()

mainloop()