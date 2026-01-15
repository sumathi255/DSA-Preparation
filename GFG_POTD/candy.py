class Solution:
    def minCandy(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: Each child gets at least one candy
        candies = [1] * n

        # Step 2: Left to right pass
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to left pass
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Total candies
        return sum(candies)


# Example usage
if __name__ == "__main__":
    arr = [1, 0, 2]
    print(Solution().minCandy(arr))
