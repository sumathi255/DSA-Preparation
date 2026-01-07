# Longest Subarray with Sum K (Positives + Negatives)

## Problem Statement
Given an array of integers (can be positive or negative) and a number K,  
find the length of the **longest contiguous subarray** whose sum equals K.

---

## Approach / Logic Explanation
- **Sliding window doesn’t work** because array may have negatives.
- Use **prefix sum + hashmap**:
  1. Maintain cumulative sum (`prefix_sum`) while traversing.
  2. Store first occurrence of each `prefix_sum` in a hashmap.
  3. If `prefix_sum - K` is already in hashmap, it means the subarray sum K exists between stored index +1 and current index.
  4. Update max length whenever we find such subarray.

---

## Algorithm
1. Initialize `prefix_sum = 0`, `max_len = 0`, and empty hashmap `sum_indices`.
2. Loop `i` from 0 to n-1:
   - Add `arr[i]` to `prefix_sum`.
   - If `prefix_sum == K`, set `max_len = i + 1`.
   - If `(prefix_sum - K)` exists in hashmap:
     - Update `max_len = max(max_len, i - sum_indices[prefix_sum - K])`.
   - Store first occurrence of `prefix_sum` in hashmap if not present.
3. Return `max_len`.

---

## Dry Run Example

### Input:
arr = [1, -1, 5, -2, 3], K = 3


### Step-by-step
| i | arr[i] | prefix_sum | prefix_sum-K | sum_indices       | max_len |
|---|--------|------------|--------------|-----------------|---------|
| 0 | 1      | 1          | -2           | {1:0}           | 0       |
| 1 | -1     | 0          | -3           | {1:0,0:1}       | 0       |
| 2 | 5      | 5          | 2            | {1:0,0:1,5:2}   | 0       |
| 3 | -2     | 3          | 0            | {1:0,0:1,5:2,3:3}| 3-1=2  |
| 4 | 3      | 6          | 3            | {1:0,0:1,5:2,3:3,6:4}| 4-3=1? check max 2 |  

**Final Output:** `4` (subarray `[1,-1,5,-2]` or `[5,-2,3]`)  

---

## Time and Space Complexity
- **Time Complexity:** O(n) → traverse array once
- **Space Complexity:** O(n) → hashmap stores prefix sums

---

## Interview Explanation (30–40 seconds)
> “I use a prefix sum and hashmap to find subarrays that sum to K.  
> As I traverse, I maintain cumulative sum. If `(prefix_sum - K)` exists, it means a subarray of sum K exists.  
> I update the maximum length. This works even with negative numbers in O(n) time and O(n) space.”

---

## Why Interviewers Ask This
- Tests **prefix sum + hashmap knowledge**
- Tests handling of **negative numbers**
- Foundation for **subarray sum problems** like count of subarrays with sum K
