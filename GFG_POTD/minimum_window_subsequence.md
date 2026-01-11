# Minimum Window Subsequence

## Problem Statement
Given two strings **s1** and **s2**, find the smallest substring in **s1**
such that **s2 appears as a subsequence** inside that substring.

- Characters of `s2` must appear **in order**
- If multiple answers exist, return the **leftmost**
- If no such substring exists, return an empty string

---

## Example

**Input**
s1 = "geeksforgeeks"
s2 = "eksrg"



**Output**
"eksforg"

---

## Approach / Logic

We use **two pointers** and solve it in **two phases**:

### 1️⃣ Forward Scan
- Traverse `s1` and try to match `s2` sequentially
- Once all characters of `s2` are matched → we found a valid window

### 2️⃣ Backward Shrinking
- Move backward from the end to remove unnecessary characters
- This gives the **minimum possible window** ending at that index

Repeat this process to find the **smallest and leftmost window**.

---

## Algorithm

1. Start pointer `i` on `s1`
2. Move forward and match `s2`
3. When fully matched, mark window end
4. Move backward to minimize window
5. Update minimum window
6. Continue searching

---

## Dry Run

### Input
s1 = geeksforgeeks
s2 = eksrg


### Forward Match
e → k → s → r → g (matched)



### Backward Shrink
eksforg (smallest valid window)


---

## Time & Space Complexity

- **Time:** `O(N × M)`
- **Space:** `O(1)`

---

## Interview Explanation (30–40 seconds)

> “I scan the first string to find a subsequence match of the second string.
Once found, I move backward to shrink the window to minimum size.
Repeating this ensures the smallest and leftmost substring containing the subsequence.”

---
