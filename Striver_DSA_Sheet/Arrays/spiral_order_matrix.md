# Spiral Order of Matrix

## 🧩 Problem Statement
Given a `n x m` matrix, return all elements in **spiral order** (clockwise).

**Example:**
Input:
[
[1,2,3],
[4,5,6],
[7,8,9]
]
Output: [1,2,3,6,9,8,7,4,5]



---

## 💡 Approach / Logic Explanation
1. Maintain four pointers: `top`, `bottom`, `left`, `right` to track boundaries.
2. Traverse the matrix in layers:
   - Top row (left → right)
   - Right column (top → bottom)
   - Bottom row (right → left)
   - Left column (bottom → top)
3. Shrink boundaries after traversing each side.
4. Repeat until all elements are visited.

---

## 🔁 Algorithm

1. Initialize `top = 0, bottom = n-1, left = 0, right = m-1`.
2. While `top <= bottom` and `left <= right`:
   - Traverse top row from `left` to `right`.
   - Increment `top`.
   - Traverse right column from `top` to `bottom`.
   - Decrement `right`.
   - If `top <= bottom`, traverse bottom row from `right` to `left`.
     - Decrement `bottom`.
   - If `left <= right`, traverse left column from `bottom` to `top`.
     - Increment `left`.
3. Return the result array.

---

## 🧪 Dry Run

**Input:**
[
[1,2,3],
[4,5,6],
[7,8,9]
]


**Step by Step:**
1. Top row → `[1,2,3]`
2. Right column → `[6,9]`
3. Bottom row → `[8,7]`
4. Left column → `[4]`
5. Remaining middle → `[5]`

**Output:** `[1,2,3,6,9,8,7,4,5]`

---

## ⏱ Time & Space Complexity
- **Time Complexity:** `O(n*m)` — each element visited once
- **Space Complexity:** `O(1)` extra (excluding output)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I maintain four pointers to track the matrix boundaries.
> I traverse the top row, right column, bottom row, and left column in sequence, shrinking the boundaries after each pass.
> This repeats until all elements are visited
> . The approach ensures we visit each element once with O(n*m) time and in-place boundary tracking.”

---
