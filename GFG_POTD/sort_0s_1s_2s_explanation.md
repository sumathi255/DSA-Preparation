# Sort 0s, 1s and 2s (Dutch National Flag Algorithm)

## Problem
Given an array consisting only of 0s, 1s, and 2s, sort the array without using extra space.

---

## Approach
I used the **Dutch National Flag Algorithm**.

I maintained three pointers:
- `low` → position for 0
- `mid` → current element
- `high` → position for 2

---

## Algorithm Logic
- If `arr[mid] == 0`  
  → swap with `arr[low]`, increment both `low` and `mid`
- If `arr[mid] == 1`  
  → just move `mid`
- If `arr[mid] == 2`  
  → swap with `arr[high]`, decrement `high`

---

## Dry Run Example

Input:
arr = [0, 2, 1, 2, 0]
------------------------------------------------------------
| low | mid | high | Array           | Action              |
|-----|-----|------|-----------------|---------------------|
| 0   | 0   | 4    | [0,2,1,2,0]     | swap low & mid      |
| 1   | 1   | 4    | [0,2,1,2,0]     | swap mid & high     |
| 1   | 1   | 3    | [0,0,1,2,2]     | swap mid & low      |
| 2   | 2   | 3    | [0,0,1,2,2]     | mid moves           |
| 2   | 3   | 3    | [0,0,1,2,2]     | swap mid & high     |
------------------------------------------------------------
Final Output:
[0, 0, 1, 2, 2]

---

## Time and Space Complexity
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**

---

## Conclusion
This approach sorts the array in a single traversal without using extra space, making it optimal.
---

## How to Explain This in an Interview (My Practice Notes)

"I solved this problem using the Dutch National Flag algorithm.
I used three pointers: low, mid, and high.

The idea is to place all 0s to the left, 1s in the middle, and 2s to the right in a single traversal.

If the current element is 0, I swap it with the low pointer and move both pointers.
If it is 1, I just move the mid pointer.
If it is 2, I swap it with the high pointer and reduce the high pointer.

This approach works in O(n) time and O(1) space, which makes it optimal."














