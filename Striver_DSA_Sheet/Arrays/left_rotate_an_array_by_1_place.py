def left_rotate(arr, n):
    # If array is empty or has only one element, no rotation needed
    if n <= 1:
        return arr

    # Store the first element temporarily
    temp = arr[0]

    # Shift all elements one position to the left
    for i in range(0, n - 1):
        arr[i] = arr[i + 1]

    # Place the first element at the last position
    arr[n - 1] = temp

    return arr

