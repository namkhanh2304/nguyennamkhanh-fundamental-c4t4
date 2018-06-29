items=["T-Shirt", "Sweater"]
buying = True
while buying:
    n=input("Welcome to our shop, what do you want (C, R, U, D)?").lower()
    if n=="r":
        print("Our items: ", *items, sep=", ")
    elif n=="c":
        item=input("Enter new item:")
        items.append(item) 
        print(*items, sep = ", ")
    elif n=="u":
        update = int(input("Update Postion:"))
        new = input("New Item:")
        items[update-1] = new
        print("Items:", *items, sep=", ")
    elif n=="d":
        del_position = input("Delete postion:")
        del items[2]
        print("Our items:", *items, sep=", ")

    else:
        print("bye bye")
        break
    
        