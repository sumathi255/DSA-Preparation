def insertion_sort(arr):
    n = len(arr)

    # Start from second element (first is already sorted)
    for i in range(1, n):

        key = arr[i]     # Element to be inserted
        j = i - 1        # Index of previous element

        # ASCENDING ORDER LOGIC:
        # Shift elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]   # Shift right
            j -= 1

        # 🔽 DESCENDING ORDER LOGIC (ONLY COMMENT):
        # while j >= 0 and arr[j] < key:
        #     arr[j + 1] = arr[j]
        #     j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr

