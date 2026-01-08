from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Count the number of subarrays whose sum equals k
        """
        n = len(nums)
        prefix_map = defaultdict(int)  # stores count of prefix sums
        prefix_sum = 0
        count = 0

        # Base case: prefix sum 0 occurs once
        prefix_map[0] = 1

        for i in range(n):
            prefix_sum += nums[i]
            # Number of times (prefix_sum - k) occurred gives subarrays ending at i with sum k
            count += prefix_map[prefix_sum - k]
            # Update the prefix sum count
            prefix_map[prefix_sum] += 1

        return count


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    result = Solution().subarraySum(nums, k)
    print("Number of subarrays with sum k:", result)
