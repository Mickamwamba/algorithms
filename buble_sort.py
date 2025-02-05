import manim

def buble_sort(arr): 
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]): 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped: 
            break
    return arr

arr = [25, 21, 22, 24, 23, 27, 26]
print(f"===> {buble_sort(arr)}")