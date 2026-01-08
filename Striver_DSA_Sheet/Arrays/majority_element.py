# ----------------------------------------------------
# Problem: Majority Element
# Algorithm: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------------------------------

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Returns the element that appears more than ⌊n/2⌋ times.
        """

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
