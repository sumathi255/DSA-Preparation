# Stock Span Problem

## Problem Statement
Given an array `arr[]` representing daily stock prices,
the **span** of a stock on day `i` is the number of consecutive days
up to day `i` (inclusive) for which the stock price is
**less than or equal to** the price on day `i`.

---

## Example

Input:
arr = [100, 80, 90, 120]

makefile
Copy code

Output:
[1, 1, 2, 4]

yaml
Copy code

---

## Key Idea

This problem is a variation of **Next Greater Element to the Left**.

We use a **monotonic decreasing stack** to keep track of indices
with higher stock prices.

---

## Approach

1. Create an empty stack to store indices
2. Traverse the array from left to right
3. While stack is not empty and current price ≥ stack top price:
   - Pop stack
4. If stack is empty:
   - Span = i + 1
5. Else:
   - Span = i − stack top index
6. Push current index into stack

---

## Algorithm

- Initialize span array
- Use stack to track previous greater prices
- Compute span using index difference
- Return span array

---

## Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Interview Tip
Say:
> "Stock Span is solved using a monotonic decreasing stack.
> It is a Next Greater Element (left side) problem."

---

## Conclusion
An efficient `O(n)` solution using stack, commonly asked in interviews.
