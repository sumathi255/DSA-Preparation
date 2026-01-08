from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        """
        Prints the subarray with maximum sum using extended Kadane's Algorithm.

        :param nums: List of integers
        :return: Subarray with maximum sum
        """

        max_sum = nums[0]
        current_sum = nums[0]

        start = 0          # temporary start index
        end = 0            # final end index
        temp_start = 0     # helps track new subarray start

        for i in range(1, len(nums)):
            # Decide whether to extend or start new subarray
            if nums[i] > current_sum + nums[i]:
                current_sum = nums[i]
                temp_start = i
            else:
                current_sum += nums[i]

            # Update max_sum and indices
            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i

        # Return the subarray with maximum sum
        return nums[start:end + 1]


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print("Maximum Subarray:", result)
    print("Maximum Sum:", sum(result))
