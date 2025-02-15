def int_polsearch(list,x ):
    idx0 = 0
    idxn = (len(list) - 1)
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
    # Find the mid point
        mid = idx0 +int(((float(idxn - idx0)/( list[idxn] - list[idx0])) * ( x - list[idx0])))
        # Compare the value at mid point with search value
        if list[mid] == x:
            return True
        if list[mid] < x:
            idx0 = mid + 1
    return False


# Example usage
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
key = 70
index = int_polsearch(arr, key)
print(f"Element found at index: {index}" if index != -1 else "Element not found")