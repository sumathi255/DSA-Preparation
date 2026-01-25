# Program to count number of valid parentheses expressions
# using Dynamic Programming (Catalan Numbers)

class Solution:
    def findWays(self, n):
        # If length is odd, valid parentheses are not possible
        if n % 2 != 0:
            return 0

        # Number of pairs of brackets
        pairs = n // 2

        # DP array to store results
        dp = [0] * (pairs + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # Fill dp array
        for i in range(2, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[pairs]
