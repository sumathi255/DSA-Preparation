# Maximum Consecutive Ones

## Problem Statement
Given a binary array (containing only 0s and 1s),  
find the **maximum number of consecutive 1s** in the array.

---

## Approach / Logic Explanation
- Traverse the array once
- Maintain:
  - `current_count` → current streak of 1s
  - `max_count` → maximum streak found so far
- If element is `1` → increase `current_count`
- If element is `0` → reset `current_count` to 0
- Update `max_count` whenever `current_count` increases

---

## Algorithm
1. Initialize `current_count = 0` and `max_count = 0`
2. Loop through each element in the array:
   - If element is `1`:
     - Increment `current_count`
     - Update `max_count`
   - Else:
     - Reset `current_count` to 0
3. Return `max_count`

---

## Dry Run Example

### Input:
nums = [1, 1, 0, 1, 1, 1]


### Step-by-step:
--------------------------------------
| Element | current_count | max_count |
|-------|---------------|-----------
| 1 |   |     1 |       |    1 |
| 1 |   |    2 |        |    2 |
| 0 |   |    0 |        |   2 |
| 1 |   |     1 |       |     2 |
| 1 |   |    2 |        |   2 |
| 1 |   |     3 |       |     3 |
-----------------------------------------
### Output:


3


---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Interview Explanation (30–40 seconds)

> “I scan the array once while maintaining a count of current consecutive 1s.  
Whenever I encounter a 1, I increment the count and update the maximum.  
If I encounter a 0, I reset the count.  
This gives an optimal O(n) time and O(1) space solution.”

---

