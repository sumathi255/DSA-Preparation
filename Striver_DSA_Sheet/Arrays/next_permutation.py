from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges numbers into the next lexicographically greater permutation.
        If such arrangement is not possible, it rearranges into the lowest order.
        """

        n = len(nums)

        # Step 1: Find the first index from the right where nums[i-1] < nums[i]
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If no such index exists, array is in descending order
        if i == 0:
            nums.reverse()
            return

        # Step 2: Find element just larger than nums[i-1] from the right
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1

        # Step 3: Swap them
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Step 4: Reverse the suffix
        nums[i:] = reversed(nums[i:])


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print("Next Permutation:", nums)
