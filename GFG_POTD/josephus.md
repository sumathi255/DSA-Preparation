# Josephus Problem (Easy Explanation)

## Problem Statement
There are `n` people standing in a circle, numbered from `1` to `n`.
Starting from person `1`, every `k`-th person is eliminated.
This process continues until only one person remains.

You need to find the position of the **last remaining person**.

---

## Example 1

Input:
n = 5, k = 2

css
Copy code

Elimination Order:
2 → 4 → 1 → 5

makefile
Copy code

Survivor:
3

yaml
Copy code

---

## Approach Used (Beginner Friendly)

We simulate the process using a list.

### Steps:
1. Store people from `1` to `n` in a list
2. Keep removing every `k`-th person using index calculation
3. Stop when only one person remains

---
Dry Run (n = 5, k = 2)
People = [1, 2, 3, 4, 5]
Remove 2 → [1, 3, 4, 5]
Remove 4 → [1, 3, 5]
Remove 1 → [3, 5]
Remove 5 → [3]


Answer = 3

Time & Space Complexity

Time Complexity: O(n²)

Space Complexity: O(n)
