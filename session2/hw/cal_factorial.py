n = int(input("enter a number:"))
factorial = 1
if n < 0:
    print("only positive numbers")
elif n == 0:
    print("factorial of 0 is 1")
else:
    for i in range (1,n+1):
        factorial = factorial*i
    print("factorial of", n, "is", factorial)