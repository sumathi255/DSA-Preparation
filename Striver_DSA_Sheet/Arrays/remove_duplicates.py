from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.
        Returns the number of unique elements.

        The first part of the array (up to returned length)
        will contain the unique elements in sorted order.
        """

        # Edge case: if array is empty, no elements to process
        if not nums:
            return 0

        # j points to the index of the last unique element
        j = 0

        # Start from second element and compare with last unique element
        for i in range(1, len(nums)):
            # If current element is different, it is a new unique element
            if nums[i] != nums[j]:
                j += 1               # move pointer for unique elements
                nums[j] = nums[i]    # place the new unique element

        # Number of unique elements = j + 1
        return j + 1


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
