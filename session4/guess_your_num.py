print("think of a number")
input()

print("""'c' if my guess is correct
's' if its smaller
'l'if its bigger""")

low=0
high=100
guess=True

while guess:
    mid=(low+high)//2
    ans = input("Is {0} your number: ".format(mid)).upper()
    if ans == "C": 
        print("im a genius")
        break
    elif ans =="L":
       high=mid
    elif ans =="S":
       low=mid
    else :
        break
