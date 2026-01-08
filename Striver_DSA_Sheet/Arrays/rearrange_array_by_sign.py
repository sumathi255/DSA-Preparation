from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearranges the array such that positive and negative numbers
        appear alternately.

        Assumption:
        - Number of positive elements == number of negative elements
        - Order of appearance is preserved
        """

        pos = []  # list to store positive numbers
        neg = []  # list to store negative numbers

        # Step 1: Separate positive and negative numbers
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        # Step 2: Place positives at even indices
        for i in range(len(pos)):
            nums[2 * i] = pos[i]

        # Step 3: Place negatives at odd indices
        for i in range(len(neg)):
            nums[2 * i + 1] = neg[i]

        return nums


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    nums = [3, -2, 1, -5, 2, -4]
    sol = Solution()
    print("Rearranged Array:", sol.rearrangeArray(nums))
