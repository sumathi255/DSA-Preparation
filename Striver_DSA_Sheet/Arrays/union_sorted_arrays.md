# Union of Two Sorted Arrays

## Problem Statement
Given two **sorted arrays**, find their **union**.  
Union means all **distinct elements** present in **either** of the arrays.

---

## Approach / Logic Explanation
Since both arrays are already sorted, we can use the **Two Pointer Technique**.

- Use two pointers:
  - `i` for first array
  - `j` for second array
- Compare elements at both pointers
- Add the smaller element to the result
- If both elements are equal, add only one
- Move pointers accordingly
- Avoid duplicates by checking the last added element

This avoids extra space like `set` and works efficiently.

---

## Algorithm
1. Initialize two pointers `i = 0`, `j = 0`
2. Create an empty list `union`
3. While both pointers are within array limits:
   - Compare `arr1[i]` and `arr2[j]`
   - Add smaller element (if not duplicate)
   - If equal, add once and move both pointers
4. Add remaining elements from both arrays
5. Return the union list

---

## Dry Run Example

### Input:
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]


### Step-by-step:


Compare 1 and 3 → add 1
Compare 2 and 3 → add 2
Compare 3 and 3 → add 3 (once)
Compare 4 and 4 → add 4
Compare 5 and 5 → add 5
Remaining → add 6, 7


### Output:


[1, 2, 3, 4, 5, 6, 7]


---

## Time and Space Complexity
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m) (for result array)

---

## Interview Explanation (30–40 seconds)

> “Since both arrays are sorted, I used the two-pointer approach.  
I compare elements from both arrays and add the smaller one to the result while avoiding duplicates.  
If both elements are equal, I add it once and move both pointers.  
This approach is efficient with linear time complexity and does not require extra data structures like sets.”

---

## When to Use This Approach
- When arrays are **already sorted**
- When interviewer restricts use of `set`
- When space optimization is required
