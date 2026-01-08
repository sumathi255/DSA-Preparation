# Rotate Image (90° Clockwise)

## 🧩 Problem Statement
Given an `n x n` 2D matrix, rotate it **90 degrees clockwise** in-place.

**Example:**
Input:
[
[1,2,3],
[4,5,6],
[7,8,9]
]
Output:
[
[7,4,1],
[8,5,2],
[9,6,3]
]

yaml
Copy code

---

## 💡 Approach / Logic Explanation
To rotate a matrix 90° clockwise in-place:

1. **Transpose the matrix**:
   - Swap `matrix[i][j]` with `matrix[j][i]`.
   - This converts rows into columns.

2. **Reverse each row**:
   - After transposing, reversing each row achieves the 90° rotation.

---

## 🔁 Algorithm

1. For each `i` from 0 to n-1:
   - For each `j` from 0 to i-1:
     - Swap `matrix[i][j]` and `matrix[j][i]` (transpose)
2. For each row in the matrix:
   - Reverse the row

---

## 🧪 Dry Run

**Input:**
[
[1,2,3],
[4,5,6],
[7,8,9]
]

markdown
Copy code

**Step 1: Transpose**
[
[1,4,7],
[2,5,8],
[3,6,9]
]

pgsql
Copy code

**Step 2: Reverse each row**
[
[7,4,1],
[8,5,2],
[9,6,3]
]

makefile
Copy code

**Output:**
[
[7,4,1],
[8,5,2],
[9,6,3]
]

yaml
Copy code

---

## ⏱ Time & Space Complexity
- **Time Complexity:** `O(n^2)` (traverse each element twice)
- **Space Complexity:** `O(1)` (in-place rotation)

---

## 🎯 Interview Explanation (30–40 seconds)

> “First, I transpose the matrix to swap rows and columns, and then I reverse each row.
>  This two-step process rotates the matrix 90° clockwise in-place without using extra space.
>  Time complexity is O(n²) and space complexity is O(1).”

---
