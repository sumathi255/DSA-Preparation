#  Max Subarray XOR of Size K

---

##  Problem Statement (Simple Words)

Given an array of integers `arr` and an integer `k`, find the **maximum XOR value** of any **contiguous subarray of size `k`**.

A subarray must contain **exactly `k` consecutive elements**.

---

##  Approach / Logic Explanation (Sliding Window + XOR)

1. First, calculate the XOR of the **first window** of size `k`.
2. Store this value as the current maximum XOR.
3. Slide the window one element at a time:
   - Remove the XOR of the element going out of the window.
   - Add the XOR of the new element coming into the window.
4. Update the maximum XOR after every slide.
5. Continue until all windows are processed.

This avoids recalculating XOR for every subarray and makes the solution efficient.

---

## 📝 Algorithm

1. Initialize `current_window_xor = 0`.
2. Compute XOR of the first `k` elements.
3. Set `max_window_xor = current_window_xor`.
4. For each index from `k` to `n-1`:
   - Update XOR using:
     ```
     current_window_xor = current_window_xor ^ arr[i] ^ arr[i-k]
     ```
   - Update `max_window_xor`.
5. Return `max_window_xor`.

---

## 🔍 Visual Dry Run Example

### Input
arr = [1, 2, 3, 4, 5]
k = 3

### Step-by-Step XOR Calculation
--------------------------------------------------------------
| Window | Elements     | XOR Calculation        | XOR Value |
|------|--------------|------------------------|-----------|
| 1    | [1, 2, 3]     | 1 ^ 2 ^ 3              | 0         |
| 2    | [2, 3, 4]     | 0 ^ 4 ^ 1              | 5         |
| 3    | [3, 4, 5]     | 5 ^ 5 ^ 2              | 2         |
-------------------------------------------------------------
### ✅ Maximum XOR
5
---

##  Edge Cases

- `k = 1` → Answer is the **maximum element** in the array.
- `k = len(arr)` → XOR of the **entire array**.
- Array with **all same elements** → XOR may become `0`.
- Minimum size array (`n = k`) → Only one window exists.

---

##  Time and Space Complexity

- **Time Complexity:** `O(n)`
  - Each element is processed once.
- **Space Complexity:** `O(1)`
  - No extra data structures used.

---

##  Interview Explanation (30–40 seconds)

> This problem is solved using the Sliding Window technique with XOR.
> First, I calculate the XOR of the initial window of size `k`.
> Then I slide the window by removing the XOR of the outgoing element and adding the XOR of the incoming element.
>  Since XOR is reversible, this operation is efficient. I track the maximum XOR value during each slide.
>  This approach runs in O(n) time and uses constant space, making it optimal.

---

## Key Interview Points

- Uses **Sliding Window**
- Efficient XOR update using `^`
- Avoids recomputation
- Optimal for large inputs
- Space optimized solution

