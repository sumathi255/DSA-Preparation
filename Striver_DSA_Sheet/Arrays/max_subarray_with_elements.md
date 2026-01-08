# Print Subarray with Maximum Subarray Sum

## 🧩 Problem Statement
Given an integer array `nums`, find the **contiguous subarray** which has the **maximum sum** and **print that subarray**.

This is an extended version of the classic **Maximum Subarray (Kadane’s Algorithm)** problem.

---

## 💡 Approach / Logic Explanation

We use **Kadane’s Algorithm** with extra variables to track:
- Start index of the best subarray
- End index of the best subarray

At each index:
- Either extend the previous subarray
- Or start a new subarray from the current element

Whenever we get a better sum, we update the subarray boundaries.

---

## 🔁 Algorithm Steps

1. Initialize:
   - `current_sum` and `max_sum` with first element
2. Maintain indices:
   - `temp_start` → possible new start
   - `start`, `end` → final subarray boundaries
3. Traverse array from index `1`
4. Decide:
   - Start new subarray if `nums[i]` is better
   - Else extend previous subarray
5. Update max sum and indices
6. Print subarray using `nums[start:end+1]`

---

## 🧪 Dry Run Example

**Input:**  
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

| Index | nums[i] | current_sum | max_sum | start-end |
|------|--------|-------------|---------|-----------|
| 0 | -2 | -2 | -2 | 0-0 |
| 1 | 1 | 1 | 1 | 1-1 |
| 2 | -3 | -2 | 1 | 1-1 |
| 3 | 4 | 4 | 4 | 3-3 |
| 4 | -1 | 3 | 4 | 3-3 |
| 5 | 2 | 5 | 5 | 3-5 |
| 6 | 1 | 6 | 6 | 3-6 |
| 7 | -5 | 1 | 6 | 3-6 |
| 8 | 4 | 5 | 6 | 3-6 |

**Output Subarray:**  
`[4, -1, 2, 1]`  
**Maximum Sum:** `6`

---

## ⏱ Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## 🎯 Interview Explanation (30–40 seconds)

> “I used Kadane’s Algorithm and extended it by tracking start and end indices.
> At each index, I decide whether to start a new subarray or extend the previous one.
> Whenever the current sum exceeds the maximum sum, I update the indices.
> Finally, I return the subarray using those indices.”

---
