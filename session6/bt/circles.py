from turtle import *

speed(-1)

color("green")
for i in range(1, 13):
    for j in range(2, i):
        circle(300/i)
mainloop()