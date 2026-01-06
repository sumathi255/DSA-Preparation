class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # j points to the position where next non-zero element should be placed
        j = 0

        # Traverse through the array
        for i in range(len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap current element with element at j
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
