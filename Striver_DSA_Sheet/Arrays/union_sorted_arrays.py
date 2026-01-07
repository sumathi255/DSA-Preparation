"""
Problem: Find Union of Two Sorted Arrays
Approach: Two Pointer Technique

"""

def find_union_sorted(arr1, arr2):
    """
    This function returns the union of two sorted arrays
    without duplicates.

    Parameters:
    arr1 -> first sorted array
    arr2 -> second sorted array

    Returns:
    A list containing union of both arrays
    """

    i = 0  # pointer for arr1
    j = 0  # pointer for arr2
    union = []

    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            # Add element if not already present
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        else:
            # Both elements are equal
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]

    print("Union of arrays:", find_union_sorted(arr1, arr2))
