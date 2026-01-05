def is_sorted(arr):
    if len(arr) < 2:
        return True  # empty or single element array is always sorted

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
