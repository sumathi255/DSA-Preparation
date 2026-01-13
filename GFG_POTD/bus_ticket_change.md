# Bus Ticket Change (Greedy Approach)

## Problem Statement
Each bus ticket costs **5 coins**.
Passengers stand in a queue and pay using notes of **5, 10, or 20** coins.

You must serve passengers in order and always give the correct change.
Return `true` if all passengers can be served, otherwise `false`.

---

## Greedy Idea
Maintain the count of:
- `five` → number of 5-coin notes
- `ten` → number of 10-coin notes

We always try to give **minimum and optimal change**.

---

## Rules
- If passenger pays **5** → no change required
- If passenger pays **10** → give **one 5**
- If passenger pays **20**:
  - Prefer **10 + 5**
  - Else give **three 5s**
  - Else → return `false`

---

## Algorithm
1. Traverse the array from left to right
2. Update note counts after each passenger
3. If change cannot be given at any step, return `false`
4. If all passengers are processed successfully, return `true`

---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Example

Input:
[5, 5, 5, 10, 20]

makefile
Copy code

Output:
true

yaml
Copy code

---

## Interview Explanation (2–3 lines)
This is a greedy simulation problem.
We track available 5 and 10 coin notes and always give optimal change.
If correct change cannot be given at any point, we immediately return false.
