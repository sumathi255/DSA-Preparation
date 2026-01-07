# ---------------------------------------------------------
# Problem: Count Distinct Elements in Every Window of Size K
# Platform: GeeksforGeeks
# Approach: Sliding Window + Hash Map (Frequency Map)
# Language: Python
# ---------------------------------------------------------

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        # Dictionary to store frequency of elements
        freq = {}

        # List to store result
        result = []

        # Variable to store count of distinct elements
        distinct_count = 0

        # ---------------- FIRST WINDOW ----------------
        for i in range(k):
            if arr[i] not in freq:
                freq[arr[i]] = 1
                distinct_count += 1
            else:
                freq[arr[i]] += 1

        result.append(distinct_count)

        # ---------------- SLIDING WINDOW ----------------
        for i in range(k, n):
            # Remove outgoing element (left side of window)
            out = arr[i - k]
            freq[out] -= 1
            if freq[out] == 0:
                distinct_count -= 1
                del freq[out]

            # Add incoming element (right side of window)
            inc = arr[i]
            if inc not in freq:
                freq[inc] = 1
                distinct_count += 1
            else:
                freq[inc] += 1

            result.append(distinct_count)

        return result


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    sol = Solution()
    print(sol.countDistinct(arr, k))  # Output: [3, 4, 4, 3]
