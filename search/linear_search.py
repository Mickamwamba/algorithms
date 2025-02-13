def linear_search(elements, item):
    found = False
    for el in elements: 
        if el == item: 
            found = True
            break
    return found

list  = [12,33,11,99,22,55,90]

print(linear_search(list,33))
print(linear_search(list,100))
