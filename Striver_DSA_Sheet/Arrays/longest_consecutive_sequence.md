# Longest Consecutive Sequence

## 🧩 Problem Statement
Given an unsorted array of integers, find the length of the **longest consecutive elements sequence**.

**Example:**
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The sequence is [1, 2, 3, 4].

markdown
Copy code

---

## 💡 Approach / Logic Explanation
1. **Sort the array** to bring consecutive elements together.
2. Initialize:
   - `lastSmaller = -inf` (keeps track of previous element)
   - `cnt = 0` (current consecutive length)
   - `longest = 1` (longest consecutive length)
3. Traverse the sorted array:
   - If `nums[i]` continues the consecutive sequence (`nums[i] - 1 == lastSmaller`), increment `cnt`.
   - Else if `nums[i]` is not duplicate, start a new sequence (`cnt = 1`).
   - Update `longest` as maximum of `longest` and `cnt`.
4. Return `longest`.

---

## 🔁 Algorithm

1. Check if array is empty → return 0
2. Sort the array
3. Initialize `lastSmaller = -inf`, `cnt = 0`, `longest = 1`
4. Loop over array:
   - If `nums[i] - 1 == lastSmaller`: `cnt += 1`, update `lastSmaller`
   - Else if `nums[i] != lastSmaller`: `cnt = 1`, update `lastSmaller`
   - Update `longest = max(longest, cnt)`
5. Return `longest`

---

## 🧪 Dry Run

**Input:** `[100, 4, 200, 1, 3, 2]`

- Step 1: Sort → `[1, 2, 3, 4, 100, 200]`
- lastSmaller = -inf, cnt = 0, longest = 1
---------------------------------------------
| i | nums[i] | lastSmaller | cnt | longest |
|---|---------|-------------|-----|---------|
|0  | 1       | -inf → 1    | 1   | 1       |
|1  | 2       | 1           | 2   | 2       |
|2  | 3       | 2           | 3   | 3       |
|3  | 4       | 3           | 4   | 4       |
|4  | 100     | 4           | 1   | 4       |
|5  | 200     | 100         | 1   | 4       |
---------------------------------------------
**Output:** 4

---

## ⏱ Time & Space Complexity
- **Time Complexity:** `O(n log n)` (sorting)  
- **Space Complexity:** `O(1)` (ignoring output)

---

## 🎯 Interview Explanation (30–40 seconds)

> “I sort the array first so that consecutive numbers come together. Then I traverse from left to right, keeping a counter for consecutive numbers. Whenever the current element continues the sequence, I increment the counter. Otherwise, I start a new sequence. I track the maximum counter to find the length of the longest consecutive sequence.”

---
