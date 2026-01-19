# Remove K Digits

## Problem Statement
Given a non-negative integer `s` as a string and an integer `k`,
remove exactly `k` digits so that the resulting number is the **smallest possible**.
The relative order of remaining digits must be preserved.

Rules:
- No leading zeros allowed
- If result is empty → return `"0"`

---

## Examples

### Example 1
Input:
s = "4325043", k = 3

makefile
Copy code
Output:
2043

makefile
Copy code

### Example 2
Input:
s = "765028321", k = 5

makefile
Copy code
Output:
221

yaml
Copy code

---

## Key Idea (Greedy + Stack)

To get the smallest number:
- Remove digits that are **bigger than the next digit**
- This creates a **monotonic increasing stack**

---

## Approach

1. Traverse digits one by one
2. While:
   - stack is not empty
   - k > 0
   - top of stack > current digit  
   → pop from stack
3. Push current digit
4. If k still > 0, remove digits from the end
5. Remove leading zeros
6. Return result or `"0"`

---

## Algorithm

- Initialize empty stack
- Iterate over string `s`
- Apply greedy popping
- Handle remaining `k`
- Strip leading zeros
- Return answer

---

## Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Interview Tip
Say:
> "This is a greedy problem solved using a monotonic increasing stack,
> similar to minimizing a number by removing digits."

---
