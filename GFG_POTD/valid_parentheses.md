# Number of Valid Parentheses

## Problem Statement
You are given a number `n`.  
Find the number of valid parentheses expressions of length `n` using only `(` and `)`.

A parentheses expression is valid if:
- Every opening bracket has a closing bracket
- Brackets are closed in the correct order

---

## Examples

| Input | Output |
|------|--------|
| n = 2 | 1 |
| n = 4 | 2 |
| n = 6 | 5 |

---

## Important Rule
- If `n` is **odd**, answer is **0**
- Valid parentheses always come in **pairs**

---

## Approach (Simple)
1. Divide `n` by 2 to get number of pairs
2. Use **Dynamic Programming**
3. The result follows **Catalan Numbers**

Formula:
dp[i] = dp[0]*dp[i-1] + dp[1]*dp[i-2] + ... + dp[i-1]*dp[0]

yaml
Copy code

---

## Time and Space Complexity
- Time Complexity: **O(n²)**
- Space Complexity: **O(n)**

---

## Conclusion
This method efficiently counts valid parentheses using DP  
and works within given constraints.
