# Best Time to Buy and Sell Stock

## 🧩 Problem Statement
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You want to **buy one day and sell on a later day** to get the **maximum profit**.

Return the maximum profit.  
If no profit is possible, return `0`.

---

## 💡 Approach / Logic Explanation

- Always try to **buy at the lowest price**
- For each day:
  - Assume you sell on that day
  - Calculate profit using the lowest buying price so far
- Keep updating the maximum profit

This ensures we check all valid buy–sell combinations in one pass.

---

## 🔁 Algorithm Steps

1. Initialize:
   - `minPrice` as infinity
   - `maxProfit` as 0
2. Traverse the prices array:
   - Update `minPrice`
   - Calculate current profit
   - Update `maxProfit`
3. Return `maxProfit`

---

## 🧪 Dry Run Example

**Input:**  
`prices = [7, 1, 5, 3, 6, 4]`

| Day | Price | minPrice | Profit | maxProfit |
|----|------|----------|--------|-----------|
| 0 | 7 | 7 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 5 | 1 | 4 | 4 |
| 3 | 3 | 1 | 2 | 4 |
| 4 | 6 | 1 | 5 | 5 |
| 5 | 4 | 1 | 3 | 5 |

**Output:** `5`

---

## ⏱ Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## 🎯 Interview Explanation (30–40 seconds)

> “I iterate through the array while keeping track of the minimum price seen so far.
> For each price, I calculate the profit if I sell on that day.
> I update the maximum profit whenever I get a better value. This works in one pass with constant space.”

---














