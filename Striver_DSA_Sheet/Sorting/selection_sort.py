def selection_sort(arr):
    n = len(arr)          # Total number of elements in the array

    # Outer loop: one by one we fix the position i
    for i in range(n):

        # Assume the current index i has the smallest element
        min_index = i

        # Inner loop: find the smallest element in the remaining unsorted array
        for j in range(i + 1, n):

            # ASCENDING ORDER LOGIC:
            # If current element is smaller than the assumed minimum,
            # update min_index
            if arr[j] < arr[min_index]:
                min_index = j

            # 🔽 DESCENDING ORDER LOGIC (ONLY COMMENT):
            # If you want DESCENDING order, change condition to:
            # if arr[j] > arr[min_index]:
            #     min_index = j
            # (We select the largest element instead of smallest)

        # Swap only if the minimum element is not already at position i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

        # After this swap:
        # - For ASCENDING → smallest element is placed at correct position
        # - For DESCENDING → largest element would be placed at correct position

    # Return the sorted array
    return arr

