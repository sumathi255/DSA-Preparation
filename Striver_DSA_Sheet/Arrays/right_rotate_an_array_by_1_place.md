Interview Explanation :

"To right rotate the array by one position, I first store the last element.
Then I shift all elements one position to the right.
Finally, I place the stored last element at index 0.

This modifies the array in-place without using extra space."
Example Dry Run

Input:

arr = [1, 2, 3, 4, 5]


Steps:

temp = 5
Shift → [1, 1, 2, 3, 4]
Place temp → [5, 1, 2, 3, 4]


Output:

[5, 1, 2, 3, 4]

⚠️ Edge Cases

[] → []

[7] → [7]

[1, 2] → [2, 1]

⏱️ Complexity

Time: O(n)

Space: O(1)

⭐ One-Line Interview Summary

"I right-rotate the array by one position using in-place shifting in O(n) time and O(1) space."
