def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i 
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [9, 8, 3, 7, 5, 6, 4, 1]

print(f"===> {selection_sort(arr)}")