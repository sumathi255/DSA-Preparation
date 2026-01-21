class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = []   # stack stores indices of days

        for i in range(n):
            # Remove elements smaller or equal to current price
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack empty → span is i+1
            if not stack:
                span[i] = i + 1
            else:
                span[i] = i - stack[-1]

            # Push current day index
            stack.append(i)

        return span
