# Expression Contains Redundant Brackets

## Problem Statement
Given a balanced expression string `s` containing characters  
`+ , - , * , / , ( , )`, check whether it contains **redundant brackets**.

Redundant brackets are unnecessary brackets that do not affect the expression.

---

## Examples

### Example 1
Input:
((a+b))

makefile
Copy code
Output:
True

makefile
Copy code
Explanation: Extra brackets around `(a+b)` are redundant.

### Example 2
Input:
(a+(b)/c)

makefile
Copy code
Output:
True

makefile
Copy code
Explanation: `(b)` is redundant.

### Example 3
Input:
(a+b+(c+d))

makefile
Copy code
Output:
False

yaml
Copy code
Explanation: All brackets are required.

---

## Approach

1. Use a **stack**
2. Push all characters except `)`
3. When `)` is encountered:
   - Pop elements until `(` is found
   - Check if there is **any operator**
4. If no operator is found → **redundant brackets**

---

## Algorithm

- Initialize empty stack
- Traverse string:
  - If character is not `)`, push to stack
  - Else:
    - Pop till `(` is found
    - Check for operator presence
    - If none found → return `True`
- If traversal completes → return `False`

---

## Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---
