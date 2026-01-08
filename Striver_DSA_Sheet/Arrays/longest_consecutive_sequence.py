from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Returns the length of the longest consecutive elements sequence.
        """

        n = len(nums)
        if n == 0:
            return 0

        # Step 1: Sort the array
        nums.sort()

        # Initialize variables
        lastSmaller = float('-inf')  # previous element in sequence
        cnt = 0                      # length of current consecutive sequence
        longest = 1                  # longest sequence found

        # Step 2: Traverse the sorted array
        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                # nums[i] continues the current consecutive sequence
                cnt += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                # nums[i] starts a new sequence
                cnt = 1
                lastSmaller = nums[i]

            # Update the longest sequence found so far
            longest = max(longest, cnt)

        return longest


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    print("Longest Consecutive Sequence Length:", Solution().longestConsecutive(arr))
