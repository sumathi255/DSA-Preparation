# Rearrange Array Elements by Sign

## 🧩 Problem Statement
Given an array `nums` containing **equal number of positive and negative integers**, rearrange the array such that:

- Positive numbers appear at **even indices**
- Negative numbers appear at **odd indices**
- Relative order of positive and negative numbers is maintained

---

## 💡 Approach / Logic Explanation

1. Separate all **positive numbers** into one list
2. Separate all **negative numbers** into another list
3. Place:
   - Positive numbers at indices `0, 2, 4, ...`
   - Negative numbers at indices `1, 3, 5, ...`

This guarantees alternating signs while preserving order.

---

## 🔁 Algorithm Steps

1. Create two empty lists: `pos` and `neg`
2. Traverse the array and store positives in `pos`, negatives in `neg`
3. Place elements of `pos` at even indices
4. Place elements of `neg` at odd indices
5. Return the modified array

---

## 🧪 Dry Run Example

**Input:**  
`nums = [3, -2, 1, -5, 2, -4]`

**Step 1: Separate**
- `pos = [3, 1, 2]`
- `neg = [-2, -5, -4]`

**Step 2: Rearranged**
Index: 0 1 2 3 4 5
Array: [3, -2, 1, -5, 2, -4]

yaml
Copy code

**Output:**  
`[3, -2, 1, -5, 2, -4]`

---

## ⏱ Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (extra arrays used)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I first separate positive and negative numbers into two lists.
>  Then I place positive numbers at even indices and negative numbers at odd indices.
> This ensures alternating signs while preserving order. The solution runs in linear time.”

---
