"""
Problem: Longest Subarray with Given Sum K (All Positives)
Approach: Sliding Window
Author: Interview Preparation
Language: Python
"""

def longest_subarray_sum_k(arr, K):
    """
    This function finds the length of the longest contiguous subarray
    with sum equal to K, assuming all elements are positive.

    Parameters:
    arr -> List of positive integers
    K   -> Target sum

    Returns:
    Length of the longest subarray
    """

    n = len(arr)
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(n):
        current_sum += arr[right]  # include arr[right] in window

        # Shrink window from left if sum > K
        while current_sum > K and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if current window sum == K
        if current_sum == K:
            max_len = max(max_len, right - left + 1)

    return max_len


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    K = 12
    print("Length of longest subarray:", longest_subarray_sum_k(arr, K))
