# Rotate Array (In-Place)

## Problem Title
Rotate Array

---

## Problem Statement (Simple Words)
You are given an array `nums` and an integer `k`.

Rotate the array to the **right by `k` steps**, and do it **in-place**:
- Do NOT use extra arrays
- Modify the original array itself
- Do not return anything

---

## Approach / Logic Explanation (Step-by-Step)

This solution uses the **Reverse Technique**.

### Key Observation:
Rotating the array to the right by `k` positions can be done by:
1. Reversing the entire array
2. Reversing the first `k` elements
3. Reversing the remaining elements

Also, we do:
k = k % len(nums)


to handle cases where `k` is greater than array size.

---

## Algorithm

1. Calculate `k = k % len(nums)`
2. Reverse the entire array
3. Reverse the first `k` elements
4. Reverse the remaining `n - k` elements
5. Array becomes rotated correctly

---

## Dry Run (Example)

**Input:**
nums = [1,2,3,4,5,6,7]
k = 3


### Step 1: Reverse entire array
[7,6,5,4,3,2,1]


### Step 2: Reverse first k = 3 elements
[5,6,7,4,3,2,1]



### Step 3: Reverse remaining elements
[5,6,7,1,2,3,4]


✅ Final rotated array.
 Time and Space Complexity

Time Complexity: O(n)
(Each element is reversed a constant number of times)

Space Complexity: O(1)
(In-place rotation, no extra space)

Interview Explanation (30–40 seconds)

“To rotate the array in-place, I used the reverse technique.
First, I reverse the entire array.
Then I reverse the first k elements and finally the remaining elements.
This achieves the right rotation in O(n) time and O(1) space, without using extra memory.”
 
