num =[-1,20,0,-10]
sorted_list = []
sorting = True

while sorting:
    min_numb= min(num)
    sorted_list.append(min_numb)
    num.remove(min_numb)

    if len(num)==0:
        break

print (*sorted_list)




