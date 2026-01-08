# Majority Element (Boyer–Moore Voting Algorithm)

## Problem Statement
Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times**.  
You may assume that the majority element **always exists** in the array.

---

## Example

### Input
nums = [2, 2, 1, 1, 1, 2, 2]

shell
Copy code

### Output
2

yaml
Copy code

---

## Brute Force Approaches

### 1. Sorting (Commented in Code)
- Sort the array
- Return element at index `n//2`

⏱ Time: `O(n log n)`  
📦 Space: `O(1)` or `O(n)` depending on sort

---

## Optimized Approach (Used)

### 🔹 Boyer–Moore Voting Algorithm

### Key Insight
If we cancel out **one majority element** with **one non-majority element**,  
the majority element will still remain in the end.

---

## Algorithm Explanation

1. Initialize:
   - `count = 0`
   - `candidate = None`
2. Traverse the array:
   - If `count == 0`, choose current element as `candidate`
   - If current element == candidate → increment count
   - Else → decrement count
3. Final `candidate` is the majority element

---

## Dry Run

### Input:
nums = [2, 2, 1, 1, 1, 2, 2]

yaml
Copy code

| num | candidate | count |
|----|----------|-------|
| 2  | 2        | 1     |
| 2  | 2        | 2     |
| 1  | 2        | 1     |
| 1  | 2        | 0     |
| 1  | 1        | 1     |
| 2  | 1        | 0     |
| 2  | 2        | 1     |

✅ Output → `2`

---

## Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Interview Explanation (30 seconds)

> "I used the Boyer–Moore Voting Algorithm.  
The idea is to cancel out different elements.  
If the count becomes zero, I choose a new candidate.  
Since the majority element appears more than n/2 times, it will always survive.  
This solution works in linear time and constant space."

---

## Edge Cases
- Single element array
- All elements are the same
- Large input size

---
