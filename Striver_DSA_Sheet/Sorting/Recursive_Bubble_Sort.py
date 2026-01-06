def bubble_sort_recursive(arr, n):
    if n == 1:
        return

    swapped = False

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    # If no swaps, array already sorted
    if not swapped:
        return

    bubble_sort_recursive(arr, n - 1)
# For descending order:
# if arr[i] < arr[i + 1]:
#     swap
