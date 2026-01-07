# Quick Sort

## Problem Statement
Given an array of integers, sort it in ascending order using **Quick Sort** algorithm.

---

## Approach / Logic Explanation
- **Quick Sort** is a **Divide and Conquer** algorithm.
- Steps:
  1. Pick a **pivot** element (commonly last element).
  2. Rearrange the array so that elements smaller than pivot go **left**, larger go **right**.
  3. Pivot is now in its correct sorted position.
  4. Recursively apply Quick Sort to left and right subarrays.
- Efficient and widely used in interviews.

---

## Algorithm
1. If array has 0 or 1 element, return (base case).
2. Call **partition** function:
   - Choose pivot.
   - Move all smaller elements to left, larger to right.
   - Return pivot index.
3. Recursively sort left and right subarrays.
4. Done.

---

## Dry Run Example

### Input:
arr = [10, 7, 8, 9, 1, 5]


### Steps:

1. Pivot = 5 → Partition → [1, 5, 8, 9, 10, 7]
2. Recursively sort left [1] → already sorted
3. Recursively sort right [8, 9, 10, 7]:
   - Pivot = 7 → Partition → [7, 9, 10, 8]
4. Recursively sort left/right of subarrays → finally sorted: [1, 5, 7, 8, 9, 10]

---

## Time and Space Complexity
- **Best Case:** O(n log n) → balanced partitions
- **Worst Case:** O(n²) → sorted or reverse-sorted input
- **Average Case:** O(n log n)
- **Space Complexity:** O(log n) → recursion stack

---

## Interview Explanation (30–40 seconds)
> “Quick Sort is a divide-and-conquer algorithm.
> I pick a pivot, partition the array into smaller and larger elements, and recursively sort both sides.
> Pivot ends up in the correct place each time. Its average time complexity is O(n log n), and it works well for large arrays.”

---
