num = int(input("Enter a number you like:"))
n = 0
for i in range (1, num):
    if number % i == 0:
        n += i

if n == num:
    print (num,"is the perfect number")
else:
    print ("this is not a perfect number")