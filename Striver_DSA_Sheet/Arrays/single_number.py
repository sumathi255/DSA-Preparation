"""
Problem: Find the Number that Appears Once
Approach: XOR Trick
Author: Interview Preparation
Language: Python
"""

def find_single_number(nums):
    """
    This function finds the element that appears only once
    in an array where every other element appears exactly twice.

    Parameters:
    nums -> List of integers

    Returns:
    Integer that appears only once
    """

    result = 0  # Initialize XOR accumulator

    for num in nums:
        # XOR of same numbers cancels out
        # 0 ^ a = a, a ^ a = 0
        result ^= num

    return result


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    nums = [2, 3, 5, 4, 5, 3, 2]
    print("Number that appears once:", find_single_number(nums))
