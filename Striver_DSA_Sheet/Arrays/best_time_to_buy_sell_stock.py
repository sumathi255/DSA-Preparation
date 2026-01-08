from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit from one buy and one sell.

        :param prices: List of stock prices
        :return: Maximum profit
        """

        maxPro = 0
        minPrice = float('inf')

        for price in prices:
            # Track minimum buying price
            minPrice = min(minPrice, price)

            # Calculate profit if sold today
            maxPro = max(maxPro, price - minPrice)

        return maxPro


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print("Maximum Profit:", sol.maxProfit(prices))
