# ----------------------------------------------------
# Problem: Two Sum
# Platform: LeetCode / GeeksforGeeks
# Approach: Hash Map (One Pass)
# Time Complexity: O(n)
# Space Complexity: O(n)
# ----------------------------------------------------

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds indices of two numbers such that they add up to target.
        """

        # Hash map to store number -> index
        hashmap = {}

        # Traverse the array
        for i, num in enumerate(nums):
            complement = target - num

            # If complement already exists, solution found
            if complement in hashmap:
                return [hashmap[complement], i]

            # Store current number with its index
            hashmap[num] = i

        # As per problem statement, exactly one solution exists
        return []
