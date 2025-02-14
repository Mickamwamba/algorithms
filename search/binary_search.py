def binary_search(elements, item): 
    found = False
    first = 0 
    last  = len(elements) - 1 

    while(first<=last and not found): 
        midpoint = (first+last)//2
        
        if elements[midpoint] == item: 
            found=True
            return found 
        else: 
            if item < elements[midpoint]: 
                last = midpoint-1
            else: 
                first = midpoint+1
    return found

list  = [12,33,11,99,22,55,90]

print(binary_search(list,33))
print(binary_search(list,100))