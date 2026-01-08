# Sort Colors (Dutch National Flag Problem)

## Problem Statement
Given an array `nums` containing only `0`, `1`, and `2`, sort the array **in-place** so that all `0`s come first, followed by `1`s, and then `2`s.

- You must not return anything
- Modify the array in-place
- Do not use built-in sort

---

## Example

**Input**
nums = [2, 0, 2, 1, 1, 0]

markdown
Copy code

**Output**
[0, 0, 1, 1, 2, 2]

markdown
Copy code

---

## Approach / Logic Explanation

This problem is solved using the **Dutch National Flag Algorithm**.

### Idea:
We divide the array into three regions:
- Left → all `0`s
- Middle → all `1`s
- Right → all `2`s

We use **three pointers**:
- `red`   → where next `0` should go
- `white` → current element being checked
- `blue`  → where next `2` should go

---

## Algorithm

1. Initialize:
   - `red = 0`
   - `white = 0`
   - `blue = n - 1`
2. While `white <= blue`:
   - If element is `0` → swap with `red`, move both pointers
   - If element is `1` → just move `white`
   - If element is `2` → swap with `blue`, move `blue`

---

## Dry Run

### Input:
nums = [2, 0, 2, 1, 1, 0]

less
Copy code

| red | white | blue | nums            | action |
|-----|-------|------|-----------------|--------|
| 0   | 0     | 5    | [2,0,2,1,1,0]   | swap 2 & 0 |
| 0   | 0     | 4    | [0,0,2,1,1,2]   | swap 0 & 0 |
| 1   | 1     | 4    | [0,0,2,1,1,2]   | move white |
| 1   | 2     | 4    | [0,0,2,1,1,2]   | swap 2 & 1 |
| 1   | 2     | 3    | [0,0,1,1,2,2]   | move white |

Final Result:
[0, 0, 1, 1, 2, 2]

yaml
Copy code

---

## Time and Space Complexity

- **Time Complexity:** `O(n)` (single pass)
- **Space Complexity:** `O(1)` (in-place)

---

## Interview Explanation (30–40 seconds)

> "I used the Dutch National Flag algorithm.  
I maintained three pointers: red for 0s, white for current element, and blue for 2s.  
While traversing the array once, I placed 0s to the left, 2s to the right, and kept 1s in the middle.  
This approach works in O(n) time and constant space."

---
