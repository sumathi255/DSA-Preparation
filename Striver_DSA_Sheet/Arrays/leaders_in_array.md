# Leaders in an Array

## 🧩 Problem Statement
Given an array of integers, find all **leaders** in the array.

👉 An element is a **leader** if it is **greater than or equal to all elements to its right side**.  
👉 The **rightmost element is always a leader**.

---

## 💡 Approach / Logic Explanation

Instead of checking every element with all elements on its right (which is slow),  
we traverse the array **from right to left** and keep track of the **maximum element seen so far**.

If the current element is greater than or equal to this maximum, it is a leader.

---

## 🔁 Algorithm

1. Initialize `max_from_right` as the last element
2. Add it to the leaders list
3. Traverse array from right to left
4. If `arr[i] >= max_from_right`
   - Update `max_from_right`
   - Add element to leaders
5. Reverse the leaders list (to maintain order)

---

## 🧪 Dry Run

**Input:**  
`arr = [16, 17, 4, 3, 5, 2]`

### Steps:

- Start from right → `2` → leader
- `5 >= 2` → leader
- `3 < 5` → not leader
- `4 < 5` → not leader
- `17 >= 5` → leader
- `16 < 17` → not leader

**Leaders (right to left):** `[2, 5, 17]`  
**Final Output:** `[17, 5, 2]`

---

## ⏱ Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (for output list)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I traverse the array from right to left while maintaining the maximum element seen so far.
> If the current element is greater than or equal to this maximum, it is a leader.
>  This approach works in linear time instead of checking every element with all elements on its right.”

---
