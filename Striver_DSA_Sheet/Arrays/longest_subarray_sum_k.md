# Longest Subarray with Given Sum K (All Positives)

## Problem Statement
Given an array of **positive integers** and a number K,  
find the length of the **longest contiguous subarray** whose sum equals K.

---

## Approach / Logic Explanation
- Since all numbers are positive, we can use **sliding window**:
  1. Keep a window defined by `left` and `right`.
  2. Add elements to the window by moving `right`.
  3. If window sum > K, shrink from the left.
  4. If window sum == K, update max length.

- Positive numbers property ensures window can only **grow or shrink**, no backtracking needed.

---

## Algorithm
1. Initialize `left = 0`, `current_sum = 0`, `max_len = 0`.
2. Loop `right` from 0 to n-1:
   - Add `arr[right]` to `current_sum`.
   - While `current_sum > K`, subtract `arr[left]` and increment `left`.
   - If `current_sum == K`, update `max_len = max(max_len, right - left + 1)`.
3. Return `max_len`.

---

## Dry Run Example

### Input:
arr = [1, 2, 3, 7, 5], K = 12


### Step-by-step
| right | arr[right] | current_sum | left | Window      | max_len |
|-------|------------|-------------|------|------------|---------|
| 0     | 1          | 1           | 0    | [1]        | 0       |
| 1     | 2          | 3           | 0    | [1,2]      | 0       |
| 2     | 3          | 6           | 0    | [1,2,3]    | 0       |
| 3     | 7          | 13          | 0→1  | [2,3,7]    | 0       |
|       |            | 12          | 1    | [2,3,7]    | 3       |
| 4     | 5          | 17          | 1→2→3| [7,5]      | 3       |
|       |            | 12          | 3    | [7,5]      | 2       |

### Output:


3


---

## Time and Space Complexity
- **Time Complexity:** O(n) → each element enters/exits window at most once
- **Space Complexity:** O(1) → only a few variables

---

## Interview Explanation (30–40 seconds)
> “I maintain a sliding window using two pointers `left` and `right`.  
> I expand the window until the sum exceeds K, then shrink from left.  
> Whenever the sum equals K, I update the maximum length.  
> This works because all numbers are positive, giving an O(n) solution with constant space.”

---

## Why Interviewers Ask This
- Tests **sliding window concept**
- Tests ability to handle **subarrays efficiently**
- Foundation for more complex **variable-size window problems**
