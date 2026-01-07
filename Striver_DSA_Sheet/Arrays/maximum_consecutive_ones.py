"""
Problem: Maximum Consecutive Ones
Approach: Single Pass (Counting)
Author: Interview Preparation
Language: Python
"""

def find_max_consecutive_ones(nums):
    """
    This function finds the maximum number of consecutive 1s in a binary array.

    Parameters:
    nums -> List of integers containing only 0s and 1s

    Returns:
    Maximum count of consecutive 1s
    """

    max_count = 0      # stores the maximum consecutive ones found
    current_count = 0  # stores current streak of 1s

    for num in nums:
        if num == 1:
            current_count += 1          # extend current streak
            max_count = max(max_count, current_count)
        else:
            current_count = 0            # reset streak when 0 appears

    return max_count


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    print("Maximum Consecutive Ones:", find_max_consecutive_ones(nums))
