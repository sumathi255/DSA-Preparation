# Next Permutation

## 🧩 Problem Statement
Given an array of integers, rearrange it into the **next lexicographically greater permutation**.
If no such permutation exists, rearrange it into the **lowest possible order (ascending)**.

---

## 💡 Approach / Logic Explanation

The idea is to modify the array in-place by following a fixed pattern:

1. Traverse from the right and find the first index where order breaks
2. Find the next greater element on the right side
3. Swap them
4. Reverse the remaining suffix

This guarantees the **next smallest greater permutation**.

---

## 🔁 Algorithm Steps

1. Start from the right and find index `i` such that `nums[i-1] < nums[i]`
2. If not found → reverse entire array
3. From the right, find element just larger than `nums[i-1]`
4. Swap these two elements
5. Reverse the subarray from index `i` till end

---

## 🧪 Dry Run Example

**Input:**  
`nums = [1, 2, 3]`

### Step 1
Find first decreasing element from right  
`2 < 3` → index = 2

### Step 2
Find just larger than `2` → `3`

### Step 3
Swap → `[1, 3, 2]`

### Step 4
Reverse suffix → `[1, 3, 2]`

✅ **Output:** `[1, 3, 2]`

---

## ⏱ Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (in-place)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I find the first decreasing element from the right, swap it with the next greater element on its right,
> and then reverse the suffix. This produces the next lexicographical permutation in linear time and constant space.”

---
