print ("sheep sizes: ")

sheep = [5, 7, 300, 90, 24, 50 ,75]
print (sheep)

for i in range (3):
    print("Month", i+1)

    print ("after shearing,this is my flock: ")
    sheep2 = [x+50 for x in sheep]
    print (sheep2)

    max_sheep = max(sheep2)
    print ("biggest sheep :", max(sheep2), "let's shear it")

    print ("After shearing, here is my flock: ")
    index = sheep2.index(max(sheep2))
    sheep2[index] = 8
    print (sheep2)

    sheep = list(sheep2)

k = sum(sheep2)
print(" total flock size: ", k)
print("I get", k, "* 2$ = ", k*2, "$")