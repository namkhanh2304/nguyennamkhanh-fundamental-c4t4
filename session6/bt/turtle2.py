from turtle import *


for i in range (4,10):
    
    for j in range (i):
        if j%2 == 0:
            color("red")
        else:
            color("blue")
        forward (50)
        left(360/i)



mainloop()