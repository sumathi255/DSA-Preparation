# Candy Distribution Problem (Greedy)

## Problem Statement
There are `n` children standing in a line, each with a rating value.
You must distribute candies such that:

1. Each child gets at least one candy
2. A child with a higher rating than an adjacent child gets more candies

Return the **minimum number of candies** required.

---

## Approach (Two-Pass Greedy)

1. Give every child **1 candy** initially
2. Traverse from **left to right**
   - If current rating is higher than left neighbor, give one more candy
3. Traverse from **right to left**
   - If current rating is higher than right neighbor, update candies using `max`
4. Sum all candies

This guarantees minimum candies while satisfying both conditions.

---

## Example

Input:
[1, 0, 2]



Output:
5

---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Interview Explanation (2–3 lines)
We assign one candy to each child initially.
Using two passes, we independently satisfy left and right neighbor conditions.
Finally, summing all candies gives the minimum required.
