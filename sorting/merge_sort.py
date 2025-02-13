def merge_sort(arr):
    print(f"Calling merge_sort({arr})")
    if(len(arr) > 1): 
        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left) #repeats until length of each list is 1
        merge_sort(right)

        a = 0
        b = 0 
        c = 0 
        print(f"Here Before Merge left= {left} vs right= {right} || mid = {mid}\n")

        while a < len(left) and b < len(right):
            if left[a] < right[b]: 
                arr[c] = left[a]
                a = a + 1
            else: 
                arr[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            arr[c]=left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            arr[c]=right[b]
            b = b + 1
            c = c + 1
    return arr


arr = [25, 21, 22, 24, 23, 27, 26]
print(f"===> {merge_sort(arr)}")
