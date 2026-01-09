class Solution:
    def countAtMostK(self, arr, k):
        """
        Function to count subarrays with at most K distinct integers.
        
        Parameters:
        arr (list): List of positive integers
        k (int): Maximum allowed distinct elements
        
        Returns:
        int: Number of subarrays with at most K distinct integers
        """
        from collections import defaultdict

        freq = defaultdict(int)
        left = 0
        distinct = 0
        count = 0

        for right in range(len(arr)):
            # Add current element to frequency map
            if freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] += 1

            # Shrink window if distinct count exceeds k
            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1

            # Count valid subarrays ending at right
            count += (right - left + 1)

        return count


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 2, 3]
    k = 2
    obj = Solution()
    print(obj.countAtMostK(arr, k))  # Output: 9
