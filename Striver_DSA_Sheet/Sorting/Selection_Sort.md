# Selection Sort

##  Problem Title
Selection Sort Algorithm

---

##  Problem Statement
Selection Sort is a simple sorting technique where we repeatedly 
select the smallest element from the unsorted part of the array and place it at the correct position in the sorted part.

---

##  Approach / Logic Explanation
- The array is divided into two parts: sorted and unsorted.
- Initially, the sorted part is empty.
- In each pass, we find the smallest element from the unsorted part.
- We swap this smallest element with the first element of the unsorted part.
- This process continues until the entire array is sorted.

---

## 📝 Algorithm
1. Find the length of the array `n`.
2. Start from index `i = 0` to `n - 1`.
3. Assume the current index has the minimum element.
4. Traverse the remaining unsorted array to find the actual minimum.
5. Update the minimum index if a smaller element is found.
6. Swap the minimum element with the element at index `i`.
7. Repeat until the array is sorted.
8. Return the sorted array.

---

##  Dry Run Example

**Input:**  
`[64, 25, 12, 22, 11]`

**Pass 1:**  
Smallest element = 11 → swap with 64  
`[11, 25, 12, 22, 64]`

**Pass 2:**  
Smallest element = 12 → swap with 25  
`[11, 12, 25, 22, 64]`

**Pass 3:**  
Smallest element = 22 → swap with 25  
`[11, 12, 22, 25, 64]`

**Final Output:**  
`[11, 12, 22, 25, 64]`

---

## Time and Space Complexity
- **Time Complexity:** O(n²) in all cases  
- **Space Complexity:** O(1) (in-place sorting)

---

## Interview Explanation (30–40 seconds)

> *Selection Sort works by dividing the array into sorted and unsorted parts.
>  In every iteration, I find the smallest element from the unsorted part and swap it with the first unsorted position.
> This continues until all elements are sorted. It is simple to implement and works in-place,
>  but it is not efficient for large datasets because it always takes O(n²) time.*

---
