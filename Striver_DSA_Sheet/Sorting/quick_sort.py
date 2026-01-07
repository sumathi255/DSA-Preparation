"""
Problem: Quick Sort
Approach: Divide and Conquer
Author: Interview Preparation Version
Language: Python
"""

def quick_sort(arr, low, high):
    """
    This function sorts the array using Quick Sort algorithm.
    
    Parameters:
    arr -> list of elements
    low -> starting index
    high -> ending index
    """

    if low < high:
        # Partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    """
    Partition function using Lomuto's scheme
    """
    pivot = arr[high]  # choose last element as pivot
    i = low - 1        # index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)

    # Descending order logic (ONLY LOGIC COMMENT):
    # if arr[j] >= pivot:
    #     i += 1
    #     arr[i], arr[j] = arr[j], arr[i]
