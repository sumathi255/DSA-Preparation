# Count Subarrays with Exactly K Odd Numbers

## Problem Statement
Given an array of positive integers and an integer `k`, count the number of **contiguous subarrays** that contain **exactly `k` odd numbers**.

---

## Example

**Input**
arr = [1, 1, 2, 1, 1]
k = 3

markdown
Copy code

**Output**
2

yaml
Copy code

---

## Approach (Step-by-Step)

Instead of checking all subarrays (brute force), we use an optimized **Sliding Window** approach.

### Key Idea:
Subarrays with exactly K odds
= Subarrays with at most K odds

Subarrays with at most (K-1) odds

yaml
Copy code

### Why this works?
- "At most K" includes all valid windows with ≤ K odd numbers
- Subtracting removes extra windows
- Remaining windows have **exactly K odds**

---

## Algorithm

1. Create a helper function `count_at_most(k)`
2. Use two pointers (`left`, `right`)
3. Expand window using `right`
4. Shrink window if odd count exceeds `k`
5. Count valid subarrays ending at `right`
6. Final answer = `atMost(k) - atMost(k-1)`

---

## Dry Run

### Input:
arr = [1, 1, 2, 1, 1], k = 3

markdown
Copy code

### Subarrays with exactly 3 odds:
- [1, 1, 2, 1]
- [1, 2, 1, 1]

### Output:
2

yaml
Copy code

---

## Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
- Single pass sliding window

---

## Interview Explanation (30–40 seconds)

> "To count subarrays with exactly K odd numbers, I used a sliding window optimization.  
Instead of checking all subarrays, I computed the number of subarrays with at most K odd numbers and subtracted the count of subarrays with at most K−1 odd numbers.  
This difference gives subarrays with exactly K odd numbers.  
The approach runs in O(n) time using two pointers and constant space, making it optimal for large inputs."

---

## Key Interview Pattern
- Sliding Window
- At Most / Exactly K trick
- Two pointers optimization

---

## When to Use This Pattern
- Exact count problems
- Subarrays with conditions
- Constraints involving `<= K`

