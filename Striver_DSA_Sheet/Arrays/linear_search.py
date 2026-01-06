def linear_search(arr, target):
    # Traverse each element in the array
    for i in range(len(arr)):
        # If target element is found
        if arr[i] == target:
            return i   # return index where target is found

    # If target is not present in the array
    return -1
