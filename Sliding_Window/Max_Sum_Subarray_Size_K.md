# Max Sum Subarray of Size K

## Problem Statement
Given an array of integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.

---

##  Approach / Logic (Sliding Window)
- First, calculate the sum of the first `k` elements.
- Store this as the initial maximum sum.
- Slide the window by:
  - Adding the next element
  - Removing the first element of the previous window
- Update the maximum sum at each step.
- This avoids recalculating the sum again and again.

---

## 📝 Algorithm
1. Compute the sum of the first `k` elements.
2. Store it as `max_sum`.
3. Move the window one step at a time.
4. Add the new element and remove the old one.
5. Update `max_sum`.
6. Return the result.

---

##  Dry Run Example

**Input:**  
`arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4`

**Step 1: Initial Window (first 4 elements)**  
`[1, 4, 2, 10] → window_sum = 1+4+2+10 = 17`  
`max_sum = 17`

**Step 2: Slide window by 1**  
`[4, 2, 10, 23] → window_sum = 17 + 23 - 1 = 39`  
`max_sum = 39`

**Step 3: Slide window by 1**  
`[2, 10, 23, 3] → window_sum = 39 + 3 - 4 = 38`  
`max_sum = 39` (no change)

**Step 4: Slide window by 1**  
`[10, 23, 3, 1] → window_sum = 38 + 1 - 2 = 37`  
`max_sum = 39` (no change)

**Step 5: Slide window by 1**  
`[23, 3, 1, 0] → window_sum = 37 + 0 - 10 = 27`  
`max_sum = 39` (no change)

**Step 6: Slide window by 1**  
`[3, 1, 0, 20] → window_sum = 27 + 20 - 23 = 24`  
`max_sum = 39` (no change)

**Final Answer:** `39`

---

##  Time and Space Complexity
- **Time Complexity:** O(n) → Each element is added and removed once
- **Space Complexity:** O(1) → No extra space used

---

##  Trace Visualization
Array: [ 1 , 4 , 2 , 10 , 23 , 3 , 1 , 0 , 20 ]
Window: [1, 4, 2, 10] -> sum = 17
Window: [4, 2, 10, 23] -> sum = 39
Window: [2, 10, 23, 3] -> sum = 38
Window: [10, 23, 3, 1] -> sum = 37
Window: [23, 3, 1, 0] -> sum = 27
Window: [3, 1, 0, 20] -> sum = 24
Max Sum = 39

---

## 🎤 Interview Explanation (30–40 seconds)

> *This problem is solved using the Sliding Window technique.
> First, I calculate the sum of the initial window of size k.
>  Then I slide the window by adding the next element and removing the previous one.
> This allows me to find the maximum sum efficiently in O(n) time instead of O(n²).
> Using the window ensures we do not recalculate sums repeatedly, which is optimal for contiguous subarray problems.*

