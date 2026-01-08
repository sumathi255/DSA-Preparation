# Maximum Subarray Sum (Kadane’s Algorithm)

## 🧩 Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

---

## 💡 Approach (Kadane’s Algorithm)

We maintain two variables:

- `current_sum` → maximum subarray sum ending at current index
- `max_sum` → maximum subarray sum found so far

At every index, we decide:
- Either extend the previous subarray
- Or start a new subarray from the current element

---

## 🔁 Algorithm Steps

1. Initialize `current_sum` and `max_sum` with the first element
2. Traverse the array from index `1`
3. Update:
current_sum = max(nums[i], current_sum + nums[i])
max_sum = max(max_sum, current_sum)

yaml
Copy code
4. Return `max_sum`

---

## 🧪 Dry Run Example

**Input:**  
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

| Index | nums[i] | current_sum | max_sum |
|------|--------|-------------|---------|
| 0 | -2 | -2 | -2 |
| 1 | 1 | 1 | 1 |
| 2 | -3 | -2 | 1 |
| 3 | 4 | 4 | 4 |
| 4 | -1 | 3 | 4 |
| 5 | 2 | 5 | 5 |
| 6 | 1 | 6 | 6 |
| 7 | -5 | 1 | 6 |
| 8 | 4 | 5 | 6 |

**Output:** `6`

---

## ⏱ Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## 🎯 Interview Explanation (Short)

> “I used Kadane’s Algorithm, where at each index
> I decide whether to extend the previous subarray or start a new one.
> I keep track of the maximum sum found so far in a single pass.”

---
