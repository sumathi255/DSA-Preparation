def merge_sort(arr):
    """
    This function sorts the array using Merge Sort algorithm
    """

    # ✅ Base case:
    # If array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # 🔹 Step 1: Divide
    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 🔹 Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 🔹 Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    This function merges two sorted arrays into one sorted array
    """

    merged = []     # Result array
    i = 0           # Pointer for left array
    j = 0           # Pointer for right array

    # 🔍 Compare elements from both arrays
    while i < len(left) and j < len(right):

        # If left element is smaller or equal
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 🧩 Add remaining elements (if any)
    # Left array remaining
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Right array remaining
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
