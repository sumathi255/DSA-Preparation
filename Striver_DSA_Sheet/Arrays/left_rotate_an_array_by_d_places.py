def reverse(arr, start, end):
    # Reverse elements between start and end indices
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def left_rotate(arr, d):
    n = len(arr)

    # Edge case: empty array
    if n == 0:
        return arr

    # Handle cases where d >= n
    d = d % n

    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse remaining n-d elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse entire array
    reverse(arr, 0, n - 1)

    return arr
