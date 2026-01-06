# Recursive Insertion Sort

---

## 1. Problem Title
Recursive Insertion Sort

---

## 2. Problem Statement (Simple Words)

Given an array of integers, sort the array in **ascending order** using the **Insertion Sort algorithm implemented recursively**.

The algorithm should:
- Use recursion instead of loops to sort the array.
- Sort the array in place without using extra space.

---

## 3. Approach / Logic Explanation (Step-by-Step)

The idea of **Recursive Insertion Sort** is similar to normal insertion sort, but instead of using loops for passes, we use recursion.

- First, we recursively sort the **first (n-1) elements** of the array.
- After that, we take the **last element** and insert it into its correct position in the already sorted part.
- This process continues until the array size becomes 1 (base case).

So at every recursive call:
- Smaller problem is solved first.
- Then the current element is placed correctly.

---

## 4. Algorithm

1. If the array size `n` is less than or equal to 1, return (already sorted).
2. Recursively sort the first `n-1` elements.
3. Store the last element in a variable.
4. Shift all elements greater than the last element one position to the right.
5. Insert the last element into its correct position.
6. Repeat until the full array is sorted.

---

## 5. Dry Run with Example

### Input:
arr = [5, 1, 4, 2, 8]


### Step-by-step Execution:

- Recursive call sorts first 4 elements: `[5, 1, 4, 2]`
- Recursive call sorts first 3 elements: `[5, 1, 4]`
- Recursive call sorts first 2 elements: `[5, 1]`
- Recursive call sorts first 1 element: `[5]` → base case

Now insertion starts:

1. Insert `1` into `[5]`  
   → `[1, 5]`

2. Insert `4` into `[1, 5]`  
   → `[1, 4, 5]`

3. Insert `2` into `[1, 4, 5]`  
   → `[1, 2, 4, 5]`

4. Insert `8` into `[1, 2, 4, 5]`  
   → `[1, 2, 4, 5, 8]`

### Output:


[1, 2, 4, 5, 8]


---

## 6. Time and Space Complexity

### Time Complexity:
- **Best Case:** O(n) (array already sorted)
- **Average Case:** O(n²)
- **Worst Case:** O(n²) (reverse sorted array)

### Space Complexity:
- **O(n)** due to recursive call stack
- No extra array is used

---

## 7. Interview Explanation (30–40 seconds)

> “Recursive insertion sort works by first sorting the first `n-1` elements of the array using recursion.
>  Once that part is sorted, the last element is inserted into its correct position by shifting larger elements to the right.
>  This process repeats until the base condition is reached when the array size becomes one.
> It is an in-place sorting algorithm, stable in nature, and works efficiently for small or nearly sorted arrays.”

---
