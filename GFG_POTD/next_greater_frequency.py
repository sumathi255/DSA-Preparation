class Solution:
    def nextGreaterFrequency(self, arr):
        n = len(arr)

        # Step 1: Frequency count
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        # Step 2: Result initialized with -1
        res = [-1] * n

        # Step 3: Stack to store indices
        stack = []

        # Step 4: Traverse array
        for i in range(n):
            # Compare frequencies
            while stack and freq[arr[i]] > freq[arr[stack[-1]]]:
                idx = stack.pop()
                res[idx] = arr[i]

            stack.append(i)

        return res
