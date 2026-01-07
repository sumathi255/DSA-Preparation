# Count Distinct Elements in Every Window of Size K

##  Problem Statement
Given an integer array `arr[]` and an integer `k`, find the count of **distinct elements** in **every contiguous subarray (window)** of size `k`.

---
##Approach / Logic Explanation

We use the **Sliding Window technique** with a **frequency map (dictionary)**.

### Key Idea:
- Store frequency of elements inside the current window
- Track distinct count separately
- Slide the window by:
  - Removing the left element
  - Adding the right element
- Update distinct count efficiently

This avoids recalculating distinct elements for every window.

---

## 🧩 Algorithm

1. Create a frequency dictionary `freq`
2. Traverse first `k` elements and populate `freq`
3. Store distinct count of first window
4. Slide the window from index `k` to `n`
   - Decrease frequency of outgoing element
   - Remove it if frequency becomes `0`
   - Add incoming element
   - Update distinct count
5. Append distinct count for each window

---

## 🔍 Dry Run Example

### Input:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

### Window-wise Processing:
-------------------------------------
| Window            | Distinct Count |
|------------------|----------------|
| [1, 2, 1, 3]     | 3              |
| [2, 1, 3, 4]     | 4              |
| [1, 3, 4, 2]     | 4              |
| [3, 4, 2, 3]     | 3              |
-------------------------------------
### Output:
[3, 4, 4, 3]

---

## ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(k)` (frequency map)

---

## 🎤 Interview Explanation (30–40 seconds)

> "This problem is solved using the sliding window technique combined with a frequency map.  
First, I calculate the frequency of elements in the first window and store the distinct count.  
Then, while sliding the window, I remove the outgoing element and add the incoming element,
> updating the frequency map accordingly.  
If an element’s frequency becomes zero, I remove it and reduce the distinct count.  
This allows me to compute the answer in linear time efficiently."

---


