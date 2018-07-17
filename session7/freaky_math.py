import function
from random import randint
from random import choice

x = randint(0,10)   
y = randint(0,10)


op= choice(["+","-","*","/"])

error=choice([-1,0,1])

res = function.cal(x, y, op)



dis_res= res + error

print ("{0} {1} {2} = {3}".format(x ,op ,y,res))

ans = input("Y/N:").lower()

if error == 0:
    if ans == "y":
        print ("correct")
    elif ans == "n":
        print ("incorrect")
else:
    if ans == "n":
        print ("correct")
    elif ans == "y":
        print ("incorrect")





