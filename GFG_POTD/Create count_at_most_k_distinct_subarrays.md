# Subarrays With At Most K Distinct Integers

## 📌 Problem Statement
Given an array of positive integers and an integer `k`, find the number of **contiguous subarrays** that contain **at most `k` distinct integers**.

---

## 🧠 Approach (Sliding Window)
We use a **two-pointer (sliding window)** technique:
- Expand the window using the `right` pointer
- Track frequency of elements using a hashmap
- Shrink the window from the `left` when distinct elements exceed `k`
- For every valid window, count all subarrays ending at `right`

---

## ✅ Algorithm Steps
1. Initialize two pointers `left` and `right`
2. Maintain a frequency map
3. Keep track of distinct elements
4. If distinct > k → shrink window
5. Add `(right - left + 1)` to answer

---

## ⏱ Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(k)`

---

## 🧪 Example

### Input
arr = [1, 2, 2, 3]
k = 2

shell
Copy code

### Output
9

shell
Copy code

### Valid Subarrays
[1], [2], [2], [3],
[1,2], [2,2], [2,3],
[1,2,2], [2,2,3]

sql
Copy code
