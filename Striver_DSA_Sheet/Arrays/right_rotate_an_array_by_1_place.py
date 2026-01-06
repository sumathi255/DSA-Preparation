def right_rotate(arr):
    n = len(arr)

    # Edge case: empty array or single element
    if n <= 1:
        return arr

    # Store the last element
    temp = arr[n - 1]

    # Shift elements one position to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Place last element at the first position
    arr[0] = temp

    return arr
