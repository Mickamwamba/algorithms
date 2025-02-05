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

# def insertion_sort_visual(arr):
#     print("Original array:", arr)
    
#     for i in range(1, len(arr)):
#         key = arr[i]  # The element to be inserted in the correct position
#         j = i - 1

#         print(f"\nInserting {key}:")
        
#         # Shift elements to the right
#         while j >= 0 and arr[j] > key:
#             print(f"  {arr[j]} > {key}, shifting {arr[j]} to position {j + 1}")
#             arr[j + 1] = arr[j]  # Move element to the right
#             j -= 1
        
#         arr[j + 1] = key  # Insert key at correct position
#         print(f"  Inserted {key} at position {j + 1}")
#         print(f"  Array after step {i}: {arr}")

# # Example usage
# arr = [8, 4, 6, 2, 9]
# insertion_sort_visual(arr)
# print("\nSorted array:", arr)
