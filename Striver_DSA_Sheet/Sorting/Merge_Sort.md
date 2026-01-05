#  Merge Sort

---

##  Problem Statement (Simple Words)

Given an array of numbers, sort the array in **ascending order** using the **Merge Sort algorithm**.

Merge Sort works by **dividing the array into smaller parts**, sorting them, and **merging them back** in sorted order.

---

##  Approach / Logic Explanation (Step-by-Step)

1. If the array has **0 or 1 element**, it is already sorted.
2. Divide the array into **two halves**.
3. Recursively apply Merge Sort on:
   - Left half
   - Right half
4. Merge the two **sorted halves**:
   - Compare elements from both arrays
   - Pick the smaller element each time
5. Continue merging until one fully sorted array is formed.

---

## 📝 Algorithm

1. If array size ≤ 1, return the array.
2. Find the middle index.
3. Split the array into left and right halves.
4. Recursively sort both halves.
5. Merge the two sorted halves into one sorted array.
6. Return the final sorted array.

---

## 🔍Dry Run Example

**Input Array:**  
[5, 1, 4, 2, 8]

### Step 1: Divide
[5, 1, 4, 2, 8]
→ [5, 1] and [4, 2, 8]
[5, 1] → [5] [1]
[4, 2, 8] → [4] [2, 8]
[2, 8] → [2] [8]
### Step 2: Merge
Merge [5] and [1] → [1, 5]
Merge [2] and [8] → [2, 8]
Merge [4] and [2, 8] → [2, 4, 8]
### Step 3: Final Merge
Merge [1, 5] and [2, 4, 8]
→ [1, 2, 4, 5, 8]

✅ **Final Sorted Array:**  
[1, 2, 4, 5, 8]
---

##  Time and Space Complexity

- **Time Complexity:**  
  - Best Case: O(n log n)  
  - Average Case: O(n log n)  
  - Worst Case: O(n log n)

- **Space Complexity:**  
  - O(n) (extra space used for merging)

---

## 🎤 Interview Explanation (30–40 seconds)

> Merge Sort is a divide and conquer algorithm.
> First, I divide the array into smaller subarrays until each contains one element. 
> Then I merge these subarrays by comparing elements and building a sorted array.
> The sorting happens during the merge step. Merge Sort always works in O(n log n) time, which makes it efficient for large datasets,
>  but it requires extra space,so it is not an in-place algorithm.

---

##  Notes for Interviews

- Merge Sort is **stable**
- It is **not in-place**
- Suitable for **large datasets**
- Guarantees **O(n log n)** time complexity
