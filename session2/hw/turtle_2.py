from turtle import *

shape("turtle")
color("red")

for i in range(4):
        forward(100)
        left(90)
color("blue")
for i in range (3):
    forward(100)
    left(360//3)
for i in range(5):
    forward(100)
    left(360//5)
color("red")
for i in range(6):
    forward(100)
    left(360//6)

mainloop()