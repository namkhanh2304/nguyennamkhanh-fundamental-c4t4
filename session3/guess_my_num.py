from random import randint
number=randint(0,100)


playing= True
times=0
while playing :
    guess=int(input("guess my number(1-100)?"))
    if guess == number:
        print ("correct")
        break
    elif guess > number:
        print("too big")
        times += 1

    else :
        print("too small")
        times += 1
    if times==7:
        print ("you lose")
        break

