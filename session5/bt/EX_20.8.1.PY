a = input("write something ")
a = a.lower()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters= {}
for i in a:
    if i in alphabet:
        if i in letters:
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1

keys = letters.keys()
for i in keys:
    print(i, letters[i],end="\t")
 