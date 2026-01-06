# Remove Duplicates from Sorted Array

## Problem Title
Remove Duplicates from Sorted Array

---

## Problem Statement (Simple Words)
You are given a **sorted array** of integers.  
Your task is to **remove duplicate elements in-place** so that each element appears only once.

- Do NOT use extra space for another array
- Modify the given array itself
- Return the number of **unique elements**
- The first `k` elements of the array should contain the unique values

---

## Approach / Logic Explanation (Step-by-Step)

Because the array is already **sorted**, all duplicate elements will be **next to each other**.

We use **two pointers**:

- `j` → keeps track of the **last unique element**
- `i` → scans the array from left to right

### Key Idea:
Whenever we find a new value different from the last unique value, we move it forward.

---

## Algorithm

1. If the array is empty, return `0`
2. Initialize pointer `j = 0` (first element is always unique)
3. Loop `i` from index `1` to end of array
4. If `nums[i] != nums[j]`:
   - Increment `j`
   - Copy `nums[i]` to `nums[j]`
5. After loop ends, return `j + 1`

---

## Dry Run (Example)

**Input:**
nums = [1, 1, 2, 2, 3]


| i | j | nums[i] | nums[j] | Action |
|---|---|--------|--------|--------|
| 1 | 0 | 1 | 1 | same → skip |
| 2 | 0 | 2 | 1 | different → j=1, nums[1]=2 |
| 3 | 1 | 2 | 2 | same → skip |
| 4 | 1 | 3 | 2 | different → j=2, nums[2]=3 |

**Final Array (first k elements):**


[1, 2, 3]


**Output:**


k = 3


---

## Time and Space Complexity

- **Time Complexity:** `O(n)`  
  (Single pass through the array)

- **Space Complexity:** `O(1)`  
  (No extra space used)

---

## Interview Explanation (30–40 seconds)

> “Since the array is sorted, all duplicates appear consecutively.  
> I use two pointers: one pointer keeps track of the last unique element, and the other pointer scans the array.  
> Whenever a new value is found, I move it forward and overwrite the duplicate.  
> This way, duplicates are removed in-place with O(1) extra space and O(n) time.”

---
