def recursive_insertion_sort(arr, n):
 
    # Base case:
    # If array has only one element, it is already sorted
    if n <= 1:
        return

    # Step 1: Sort first (n-1) elements using recursion
    recursive_insertion_sort(arr, n - 1)

    # Step 2: Insert the last element at correct position
    last = arr[n - 1]      # element to be inserted
    j = n - 2              # index of previous element

    # Move elements greater than last one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    # Place last element at its correct position
    arr[j + 1] = last


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    recursive_insertion_sort(arr, len(arr))
    print("Sorted Array:", arr)

    # Descending order logic (ONLY LOGIC COMMENT):
    # while j >= 0 and arr[j] < last:
    #     arr[j + 1] = arr[j]
