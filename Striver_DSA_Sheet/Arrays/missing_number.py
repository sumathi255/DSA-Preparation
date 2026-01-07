"""
Problem: Find Missing Number in an Array
Approach: XOR Technique
Language: Python
"""

def find_missing_number(arr, n):
    """
    This function finds the missing number in an array
    containing numbers from 1 to n with one missing.

    Parameters:
    arr -> list of integers (size n-1)
    n   -> range of numbers from 1 to n

    Returns:
    Missing number
    """

    xor_all = 0      # XOR of numbers from 1 to n
    xor_arr = 0      # XOR of array elements

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all elements in array
    for num in arr:
        xor_arr ^= num

    # Missing number is XOR of above two
    return xor_all ^ xor_arr


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6]
    n = 6
    print("Missing Number:", find_missing_number(arr, n))
