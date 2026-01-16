class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []

        # Step 1: Build intervals
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))

        # Step 2: Sort intervals by start time
        intervals.sort()

        count = 0
        idx = 0
        covered_end = 0

        # Step 3: Greedy interval covering
        while covered_end < n:
            farthest = covered_end

            while idx < len(intervals) and intervals[idx][0] <= covered_end:
                farthest = max(farthest, intervals[idx][1] + 1)
                idx += 1

            if farthest == covered_end:
                return -1

            count += 1
            covered_end = farthest

        return count
