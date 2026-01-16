# Minimum Number of Workers (Greedy Interval Covering)

## Problem Summary
You are given an array `arr[]` where:
- `arr[i] != -1` means the person at index `i` can cover the interval  
  `[i - arr[i], i + arr[i]]`
- `arr[i] == -1` means the person is unavailable

The goal is to cover the entire working day `[0 ... n-1]`
using the **minimum number of people**.

If full coverage is impossible, return `-1`.

---

## Key Idea
This is a **minimum interval covering** problem.

### Strategy
1. Convert each valid person into a coverage interval.
2. Clamp intervals to valid bounds `[0, n-1]`.
3. Sort intervals by start time.
4. Use a **greedy approach**:
   - Always select the interval that starts before the current coverage
     and extends the coverage the farthest.

---

## Why Greedy Works
At each step, choosing the interval with the farthest reach ensures
minimum selections while maintaining continuous coverage.

---

## Time & Space Complexity
- **Time:** `O(n log n)` (due to sorting)
- **Space:** `O(n)` (interval storage)

---

## Example Walkthrough

### Input
arr = [1, 2, 1, 0]

makefile
Copy code

Intervals:
Index 0 → [0,1]
Index 1 → [0,3]
Index 2 → [1,3]
Index 3 → [3,3]

yaml
Copy code

Greedy choice:
- Pick `[0,3]` → fully covers `[0...3]`

**Answer = 1**

---

## Edge Cases
- Gaps in coverage → return `-1`
- All `-1` values → return `-1`
- Single interval covering whole day → return `1`

---

## Interview Tip
Mention:
> “This is a classic greedy interval covering problem similar to minimum taps / minimum platforms.”

That instantly signals strong problem recognition.
