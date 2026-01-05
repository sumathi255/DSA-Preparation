Edge Cases

Empty array: [] → return None

Single element: [5] → return None

All elements same: [2, 2, 2] → return None

Negative numbers: [-5, -1, -9] → return -5

Mixed numbers: [3, 1, 4, 4, 2] → return 3

Interview Explanation

"To find the second largest element, I keep track of two variables: max_val for the largest element and second_max for the second largest.
I iterate through the array:

If the current number is greater than max_val, I update second_max with max_val and then update max_val.

If the current number is not equal to max_val but greater than second_max, I update second_max.

At the end, second_max contains the second largest element.

I handle edge cases:

If the array has less than 2 unique elements, I return None.

Works for negative numbers and arrays with duplicate values."
