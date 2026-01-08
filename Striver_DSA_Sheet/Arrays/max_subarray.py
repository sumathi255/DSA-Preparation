from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the maximum subarray sum using Kadane's Algorithm.

        :param nums: List of integers
        :return: Maximum subarray sum
        """

        # Initialize both current and maximum sum
        max_sum = nums[0]
        current_sum = nums[0]

        # Traverse from the second element
        for i in range(1, len(nums)):
            # Either extend the previous subarray or start new
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
