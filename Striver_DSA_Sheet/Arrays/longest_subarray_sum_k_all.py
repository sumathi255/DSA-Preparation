"""
Problem: Longest Subarray with Given Sum K (Positives + Negatives)
Approach: Prefix Sum + HashMap
Author: Interview Preparation
Language: Python
"""

def longest_subarray_sum_k(arr, K):
    """
    This function finds the length of the longest contiguous subarray
    with sum equal to K, works for positive and negative numbers.

    Parameters:
    arr -> List of integers (positive/negative)
    K   -> Target sum

    Returns:
    Length of the longest subarray
    """

    prefix_sum = 0
    max_len = 0
    sum_indices = {}  # store first occurrence of prefix sum

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If prefix_sum == K, subarray from 0 to i
        if prefix_sum == K:
            max_len = i + 1

        # If (prefix_sum - K) seen before, update max_len
        if (prefix_sum - K) in sum_indices:
            max_len = max(max_len, i - sum_indices[prefix_sum - K])

        # Store first occurrence of prefix_sum
        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i

    return max_len


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [1, -1, 5, -2, 3]
    K = 3
    print("Length of longest subarray:", longest_subarray_sum_k(arr, K))
