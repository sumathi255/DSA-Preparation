# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to the target.

- Each input has **exactly one solution**
- You cannot use the same element twice
- Answer can be returned in any order

---

## Example

**Input**
nums = [2, 7, 11, 15]
target = 9

markdown
Copy code

**Output**
[0, 1]

markdown
Copy code

**Explanation**
nums[0] + nums[1] = 2 + 7 = 9

yaml
Copy code

---

## Approach / Logic Explanation

Instead of checking all pairs (brute force), we use a **Hash Map** to store numbers we have already seen.

### Idea:
- For every number `num`, calculate `target - num`
- If that value already exists in the map, we found the answer
- Otherwise, store the current number with its index

This allows us to solve the problem in **one pass**.

---

## Algorithm

1. Create an empty hash map
2. Traverse the array using index and value
3. Calculate `complement = target - current number`
4. If complement exists in map → return indices
5. Else store current number with index in map

---

## Dry Run

### Input:
nums = [2, 7, 11, 15], target = 9

yaml
Copy code
-------------------------------------------------
| i | num | complement | hashmap       | action |
|---|-----|------------|---------------|--------|
| 0 | 2   | 7          | {}            | store 2 |
| 1 | 7   | 2          | {2:0}         | found → return [0,1] |
---------------------------------------------------
---

## Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
- Single traversal using hash map

---

## Interview Explanation (30–40 seconds)

> "I solved Two Sum using a hash map.  
While traversing the array, for each element I calculate its complement as `target - current number`.  
If the complement already exists in the map, I return the indices.  
Otherwise, I store the current number with its index.  
This approach runs in O(n) time and uses O(n) extra space, which is optimal compared to brute force."

---
