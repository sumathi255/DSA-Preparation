# Find the Number that Appears Once (All Others Twice)

## Problem Statement
Given an array of integers where **every element appears twice except for one element**.  
Find the element that appears only once.

---

## Approach / Logic Explanation
- Use the **XOR trick**:
  1. XOR of a number with itself is 0 → `a ^ a = 0`
  2. XOR of a number with 0 is the number itself → `0 ^ a = a`
- Traverse the array and XOR all elements:
  - All numbers appearing twice will cancel each other
  - Only the single number remains

---

## Algorithm
1. Initialize `result = 0`
2. Loop through each element `num` in the array:
   - `result = result ^ num`
3. Return `result`

---

## Dry Run Example

### Input:
nums = [2, 3, 5, 4, 5, 3, 2]


### Step-by-step XOR:
| Step | Operation | Result |
|------|-----------|--------|
| 0    | 0 ^ 2     | 2      |
| 1    | 2 ^ 3     | 1      |
| 2    | 1 ^ 5     | 4      |
| 3    | 4 ^ 4     | 0      |
| 4    | 0 ^ 5     | 5      |
| 5    | 5 ^ 3     | 6      |
| 6    | 6 ^ 2     | 4      |

### Output:


4


---

## Time and Space Complexity
- **Time Complexity:** O(n) → traverse array once
- **Space Complexity:** O(1) → only one variable used

---

## Interview Explanation (30–40 seconds)
> “I iterate over the array and XOR all elements. XOR cancels out numbers appearing twice.  
> So, the number that appears only once remains. This solution is optimal with O(n) time and O(1) space.”

---

## Why Interviewers Ask This
- Tests **bit manipulation knowledge**
- Tests **linear scan** with O(1) space
- Foundation for **more advanced XOR problems** in interviews
