Edge Cases to Cover

Empty array: [] → return None or handle exception

Single element array: [5] → return 5

All elements same: [2, 2, 2, 2] → return 2

Negative numbers: [-5, -1, -9] → return -1

Mixed positive & negative: [-5, 0, 3, 2] → return 3
Interview Explanation (Step by Step)

If interviewer asks, ila explain cheyyachu:

"I am finding the largest element in the array by iterating through each element and keeping track of the maximum seen so far.
I initialize the maximum with the first element, then compare it with the remaining elements one by one.
If a larger element is found, I update the maximum.
At the end of the loop, the variable contains the largest element.

I also handle edge cases:

If the array is empty, I return None or throw an error.

Works for negative numbers and arrays with all equal elements."
