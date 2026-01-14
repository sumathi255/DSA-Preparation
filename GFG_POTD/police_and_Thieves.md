# Police and Thieves (Greedy + Two Pointers)

## Problem Statement
You are given an array where:
- 'P' represents a policeman
- 'T' represents a thief

Each policeman can catch **only one thief**.
A thief can be caught only if the distance between them is **≤ k**.

Your task is to find the **maximum number of thieves** that can be caught.

---

## Approach
This problem is solved using a **greedy two-pointer technique**.

### Steps
1. Store indices of all policemen in one list
2. Store indices of all thieves in another list
3. Use two pointers to compare positions
4. If distance ≤ k → catch thief and move both pointers
5. Otherwise, move the pointer with the smaller index

---

## Why Greedy Works
Matching the closest possible policeman and thief first ensures
maximum number of valid catches.

---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## Example

Input:
arr = ['P', 'T', 'T', 'P', 'T']
k = 1

makefile
Copy code

Output:
2

yaml
Copy code

---

## Interview Explanation (2–3 lines)
We store positions of policemen and thieves separately.
Using two pointers, we greedily match the nearest possible thief
within distance `k` to maximize the number of catches.
