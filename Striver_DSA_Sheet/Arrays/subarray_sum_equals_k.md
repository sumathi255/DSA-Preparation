# Subarray Sum Equals K

## 🧩 Problem Statement
Given an array of integers `nums` and an integer `k`, return the **number of subarrays** whose sum equals `k`.

**Example:**
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays [1,1] and [1,1] (starting at index 0 and 1) sum to 2.

yaml
Copy code

---

## 💡 Approach / Logic Explanation
1. Use **prefix sum** to keep track of sums up to each index.
2. Maintain a **hashmap** that stores frequency of prefix sums.
3. For each element:
   - Add it to the current prefix sum.
   - If `(prefix_sum - k)` exists in the hashmap, add its frequency to the result.
   - Increment the frequency of `prefix_sum` in the hashmap.

> This works because `prefix_sum[i] - prefix_sum[j] = k` means the subarray `nums[j+1..i]` has sum `k`.

---

## 🔁 Algorithm

1. Initialize `prefix_map = {0: 1}` and `prefix_sum = 0, count = 0`.
2. Loop through the array:
   - `prefix_sum += nums[i]`
   - `count += prefix_map[prefix_sum - k]`
   - `prefix_map[prefix_sum] += 1`
3. Return `count`.

---

## 🧪 Dry Run

**Input:** nums = [1,1,1], k = 2

| i | nums[i] | prefix_sum | prefix_sum - k | count | prefix_map          |
|---|----------|------------|----------------|-------|-------------------|
| 0 | 1        | 1          | -1             | 0     | {0:1, 1:1}        |
| 1 | 1        | 2          | 0              | 1     | {0:1, 1:1, 2:1}   |
| 2 | 1        | 3          | 1              | 2     | {0:1, 1:1, 2:1, 3:1} |

**Output:** 2

---

## ⏱ Time & Space Complexity
- **Time Complexity:** O(n) — single pass through array
- **Space Complexity:** O(n) — hashmap stores prefix sums

---

## 🎯 Interview Explanation (30–40 seconds)

> “We use prefix sums and a hashmap to count subarrays with sum `k`.
> At each index, we calculate the prefix sum. If `(prefix_sum - k)` exists in the hashmap,
> it means a subarray ending at this index has sum `k`. We update the hashmap for future calculations.
>  This solution runs in O(n) time and is optimal for large arrays.”

---
