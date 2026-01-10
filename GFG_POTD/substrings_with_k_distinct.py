class Solution:
    def countSubstr(self, s, k):
        """
        Counts the number of substrings with exactly k distinct characters.
        """

        def atMostK(s, k):
            if k < 0:
                return 0

            freq = {}
            left = 0
            distinct = 0
            count = 0

            for right in range(len(s)):
                if freq.get(s[right], 0) == 0:
                    distinct += 1
                freq[s[right]] = freq.get(s[right], 0) + 1

                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1

                # Count substrings ending at 'right'
                count += (right - left + 1)

            return count

        return atMostK(s, k) - atMostK(s, k - 1)


# Example usage (for local testing)
if __name__ == "__main__":
    s = "aba"
    k = 2
    ob = Solution()
    print(ob.countSubstr(s, k))  # Output: 3
