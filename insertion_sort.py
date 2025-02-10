def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n): 
        j = i-1 # the previous index 
        next = arr[i]

        while(arr[j] > next and j>=0):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = next
    return arr

arr = [25, 21, 22, 24, 23, 27, 26]
print(f"===> {insertion_sort(arr)}")