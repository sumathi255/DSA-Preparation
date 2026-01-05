# Bubble Sort

## 📌 Problem Statement
Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and
swaps them if they are in the wrong order, until the array becomes sorted.

---

## 🧠 Approach / Logic
- I perform multiple passes over the array.
- In each pass, adjacent elements are compared.
- If the left element is greater than the right one, they are swapped.
- After each pass, the largest element moves to the end.
- An optimization is used to stop early if no swaps occur in a pass.

---

## 📝 Algorithm
1. Get the length of the array `n`.
2. Run an outer loop for `n` passes.
3. Initialize a `swapped` flag as `False`.
4. Compare adjacent elements in the inner loop.
5. Swap if elements are in the wrong order.
6. If no swaps happen in a pass, break the loop.
7. Return the sorted array.

---

## 🔍 Dry Run Example

**Input:**  
`[5, 1, 4, 2, 8]`

**Pass 1:**  
Compare 5 & 1 → swap → `[1, 5, 4, 2, 8]`  
Compare 5 & 4 → swap → `[1, 4, 5, 2, 8]`  
Compare 5 & 2 → swap → `[1, 4, 2, 5, 8]`  
Compare 5 & 8 → no swap  

**Pass 2:**  
Array becomes more sorted.

**Final Output:**  
`[1, 2, 4, 5, 8]`

---

## ⏱️ Time and Space Complexity
- **Time Complexity:**  
  - Worst Case: O(n²)  
  - Best Case (already sorted): O(n)
- **Space Complexity:**  
  - O(1) (in-place sorting)

---

## 🎤 How to Explain in an Interview (30–40 seconds)

> *I used Bubble Sort, where I repeatedly compare adjacent elements and swap them if they are in the wrong order.
> After each pass, the largest element moves to the end. I also used a swapped flag as an optimization to stop early when the array is already sorted.
> This improves performance for nearly sorted arrays.*


