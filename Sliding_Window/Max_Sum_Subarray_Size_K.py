class Solution:
    def maxSubarraySum(self, arr, k):
        # Step 1: Calculate the sum of the first 'k' elements
        # This will be our initial window sum
        window_sum = sum(arr[:k])
        max_sum = window_sum  # Initialize max_sum with the first window sum

        # Step 2: Slide the window across the array
        # Start from index 'k' to the end of the array
        for i in range(k, len(arr)):
            # Update the window sum by:
            # 1. Adding the new element entering the window (arr[i])
            # 2. Subtracting the element leaving the window (arr[i - k])
            window_sum = window_sum + arr[i] - arr[i - k]

            # Step 3: Update max_sum if the new window_sum is greater
            max_sum = max(max_sum, window_sum)

        # Step 4: Return the maximum sum found
        return max_sum
