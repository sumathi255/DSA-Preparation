# Minimum Window Subsequence
# Interview-ready implementation
# Time Complexity: O(N * M)
# Space Complexity: O(1)

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        min_len = float('inf')
        start_index = -1

        i = 0
        while i < n:
            # ---------- Forward scan ----------
            j = 0
            while i < n:
                if s1[i] == s2[j]:
                    j += 1
                    if j == m:
                        break
                i += 1

            # If s2 not fully matched
            if j < m:
                break

            end = i  # window end index

            # ---------- Backward shrink ----------
            j = m - 1
            while i >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                    if j < 0:
                        break
                i -= 1

            start = i  # correct start index

            # Update minimum window
            window_len = end - start + 1
            if window_len < min_len:
                min_len = window_len
                start_index = start

            # Move forward to find next possible window
            i = start + 1

        if start_index == -1:
            return ""

        return s1[start_index : start_index + min_len]


# ---------------- Example ----------------
if __name__ == "__main__":
    s1 = "geeksforgeeks"
    s2 = "eksrg"
    print(Solution().minWindow(s1, s2))  # Output: eksforg
