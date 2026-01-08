# ----------------------------------------------------
# Problem: Sort Colors (Dutch National Flag Algorithm)
# Platform: LeetCode / GeeksforGeeks
# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------------------------------

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the array containing 0s, 1s, and 2s in-place.
        """

        # red   -> position for next 0
        # white -> current index
        # blue  -> position for next 2
        red = 0
        white = 0
        blue = len(nums) - 1

        # Process elements until white crosses blue
        while white <= blue:
            if nums[white] == 0:
                # Swap current element with red pointer
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1

            elif nums[white] == 1:
                # 1 is already in correct region
                white += 1

            else:
                # nums[white] == 2
                # Swap with blue pointer
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
