# Set Matrix Zeroes

## 🧩 Problem Statement
Given a `m x n` matrix, if an element is `0`, set its entire row and column to `0`. Modify the matrix **in-place**.

**Example:**
Input:
[
[1,1,1],
[1,0,1],
[1,1,1]
]
Output:
[
[1,0,1],
[0,0,0],
[1,0,1]
]

yaml
Copy code

---

## 💡 Approach / Logic Explanation
1. Use **first row and first column** as markers for which row/column should be zeroed.
2. Keep a separate flag `col0` for the first column (since `matrix[0][0]` is shared with first row).
3. Traverse the matrix:
   - If `matrix[i][j] == 0`, mark `matrix[i][0] = 0` (row) and `matrix[0][j] = 0` (column).
   - If `j == 0`, update `col0 = 0`.
4. Iterate matrix again (excluding first row & column):
   - If `matrix[i][0] == 0` or `matrix[0][j] == 0`, set `matrix[i][j] = 0`.
5. Handle first row and first column separately using the markers.

---

## 🔁 Algorithm

1. Initialize `col0 = 1`.
2. First pass: mark rows and columns where zeros appear.
3. Second pass: set `matrix[i][j] = 0` using markers (skip first row & column).
4. Set first row to 0 if `matrix[0][0] == 0`.
5. Set first column to 0 if `col0 == 0`.

---

## 🧪 Dry Run

**Input:**  
[
[1, 2, 3],
[4, 0, 6],
[7, 8, 9]
]

sql
Copy code

**Step 1:** Mark zeros in first row/column  
matrix[1][0] = 0 (mark row)
matrix[0][1] = 0 (mark column)

powershell
Copy code

**Step 2:** Update matrix using markers  
[
[1,0,3],
[0,0,0],
[7,0,9]
]

sql
Copy code

**Step 3:** Update first row/column if needed (already done for column 0, row 0 is fine)

**Output:**  
[
[1,0,3],
[0,0,0],
[7,0,9]
]

yaml
Copy code

---

## ⏱ Time & Space Complexity
- **Time Complexity:** `O(m*n)` (traverse matrix twice)
- **Space Complexity:** `O(1)` (in-place, only a few variables)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I use the first row and first column as markers to track which rows and columns should be zeroed.
> A separate flag is used for the first column. First I mark all rows and columns with zeros,
>  then I update the matrix based on the markers, and finally handle the first row and column separately.
>  This ensures an in-place O(1) extra space solution.”

---
