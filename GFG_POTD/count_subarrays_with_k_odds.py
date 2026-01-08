# ----------------------------------------------------
# Problem: Count Subarrays with Exactly K Odd Numbers
# Platform: GeeksforGeeks
# Approach: Sliding Window (At Most K trick)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------------------------------

class Solution:
    def countSubarray(self, arr, k):
        """
        Counts subarrays with exactly k odd numbers.
        """

        # Helper function to count subarrays with AT MOST k odd numbers
        def count_at_most(k):
            left = 0
            odd_count = 0
            total_subarrays = 0

            # Expand window using right pointer
            for right in range(len(arr)):
                # If current element is odd, increase odd count
                if arr[right] % 2 == 1:
                    odd_count += 1

                # Shrink window until odd_count <= k
                while odd_count > k:
                    if arr[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                # All subarrays ending at 'right' are valid
                total_subarrays += (right - left + 1)

            return total_subarrays

        # Exactly K odds = AtMost(K) - AtMost(K-1)
        return count_at_most(k) - count_at_most(k - 1)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 1]
    k = 3
    obj = Solution()
    print("Count of subarrays:", obj.countSubarray(arr, k))
