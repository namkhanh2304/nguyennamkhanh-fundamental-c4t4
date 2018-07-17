x = int(input("x = "))
operation= input ("operation(+,-,*,/):")
y = int(input("y = "))

if operation == "+":
    res = x + y
elif operation == "-":
    res = x - y
elif operation == "*":
    res = x * y
elif operation == "/":
    res = x / y

print ("{0} {1} {2} = {3}".
    format(x,operation,y,res))