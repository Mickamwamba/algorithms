def shell_sort(arr):
    distance = len(arr)//2

    while distance > 0: 
        for i in range(distance, len(arr)): 
            temp = arr[i]
            j = i 
            # Sort the sublists for this distance: 
            while (j>=distance and arr[j-distance] > temp): 
                arr[j] = arr[j-distance] 
                j = j - distance
            arr[j] = temp 
            # Reducing the distance for the next distance 
        distance = distance // 2 
    return arr



arr = [25, 21, 22, 24, 23, 27, 26]
print(f"===> {shell_sort(arr)}")