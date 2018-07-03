prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock ={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    print(key)
    print ("price:{} ".format(prices[key]))
    print ("stock:{} ".format(stock[key]))
 
total = (4*6+2*0+1.5*32+3*15)

print("Total:", total,"$")  
