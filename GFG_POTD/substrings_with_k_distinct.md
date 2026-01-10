# Substrings with Exactly K Distinct Characters

## 📌 Problem Statement
Given a string `s` consisting of lowercase letters and an integer `k`,
count the number of **substrings** that contain **exactly `k` distinct characters**.

---

## 🧠 Key Insight
To find substrings with **exactly K distinct characters**, we use the formula:

Exactly K = At Most K − At Most (K − 1)

yaml
Copy code

This converts the problem into a **sliding window** problem.

---

## 🔁 Sliding Window Approach
1. Use two pointers (`left` and `right`)
2. Maintain a frequency map of characters
3. Expand window with `right`
4. Shrink window from `left` if distinct characters exceed `k`
5. For every valid window, add `(right - left + 1)` substrings

---

## 🧪 Example

### Input
s = "aba"
k = 2

shell
Copy code

### Output
3

shell
Copy code

### Valid Substrings
"ab", "ba", "aba"

yaml
Copy code

---

## ⏱ Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(26)` (constant, lowercase letters)
