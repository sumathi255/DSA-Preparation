# Insertion Sort

## 📌 Problem Title
Insertion Sort Algorithm

---

## 📖 Problem Statement
Insertion Sort is a sorting algorithm where elements are picked one by one and placed
into their correct position in the already sorted part of the array.

---

## Approach / Logic Explanation
- The array is divided into two parts: sorted and unsorted.
- Initially, the first element is considered sorted.
- We take the next element from the unsorted part.
- This element is compared with elements in the sorted part.
- Larger elements are shifted to the right to make space.
- The element is inserted at its correct position.
- This process repeats until the array is completely sorted.

---

## 📝 Algorithm
1. Start from the second element of the array.
2. Store the current element as `key`.
3. Compare `key` with elements before it.
4. Shift all elements greater than `key` one position to the right.
5. Insert `key` at the correct position.
6. Repeat for all elements.
7. Return the sorted array.

---

##  Dry Run Example

**Input:**  
`[12, 11, 13, 5, 6]`

**Pass 1:**  
Key = 11 → Insert before 12  
`[11, 12, 13, 5, 6]`

**Pass 2:**  
Key = 13 → Already in correct position  
`[11, 12, 13, 5, 6]`

**Pass 3:**  
Key = 5 → Insert at beginning  
`[5, 11, 12, 13, 6]`

**Pass 4:**  
Key = 6 → Insert between 5 and 11  
`[5, 6, 11, 12, 13]`

**Final Output:**  
`[5, 6, 11, 12, 13]`

---

##  Time and Space Complexity
- **Time Complexity:**  
  - Worst Case: O(n²)  
  - Best Case (already sorted): O(n)
- **Space Complexity:**  
  - O(1) (in-place sorting)

---

## 🎤 Interview Explanation (30–40 seconds)

> *Insertion Sort works by taking one element at a time and inserting it into its correct position
> in the sorted part of the array. The first element is assumed to be sorted, and for each next element,
> larger values are shifted to the right to make space. It is easy to implement and efficient for small or nearly sorted datasets,
>  but it is not suitable for large datasets due to its O(n²) time complexity.*

---
