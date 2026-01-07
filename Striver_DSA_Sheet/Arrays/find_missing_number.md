# Find Missing Number in an Array

## Problem Statement
You are given an array containing numbers from **1 to n**, but **one number is missing**.  
Find the missing number.

---

## Approach / Logic Explanation (XOR Method)

- XOR of a number with itself is `0`
- XOR of a number with `0` is the number itself
- If we XOR all numbers from `1 to n` and XOR all array elements,
  the duplicate numbers cancel out
- The remaining value is the missing number

This avoids overflow and extra space.

---

## Algorithm
1. Initialize `xor_all = 0`
2. XOR all numbers from `1` to `n`
3. Initialize `xor_arr = 0`
4. XOR all elements of the array
5. XOR both results → missing number

---

## Dry Run Example

### Input:
arr = [1, 2, 4, 5, 6]
n = 6


### XOR from 1 to 6:


1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 = X


### XOR of array:


1 ^ 2 ^ 4 ^ 5 ^ 6 = Y


### Final:


X ^ Y = 3 (missing number)


---

## Time and Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Interview Explanation (30–40 seconds)

> “I used the XOR approach.  
I XOR all numbers from 1 to n and XOR all elements in the array.  
Since XOR cancels identical numbers, all present numbers cancel out.  
The remaining value is the missing number.  
This runs in linear time and constant space, which is optimal.”

---

## Why Interviewers Like This
- Tests bit manipulation knowledge
- No extra space
- No overflow issues like sum formula
