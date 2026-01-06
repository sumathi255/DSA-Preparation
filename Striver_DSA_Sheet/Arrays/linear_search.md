Interview Explanation (How to Say)

"In linear search, I check each element of the array one by one.
If the target element matches the current element, I return its index.
If I reach the end of the array without finding the target, I return -1.

Linear search works for both sorted and unsorted arrays."
Dry Run Example

Input:

arr = [4, 2, 7, 1, 9]
target = 7


Steps:

i=0 → 4 != 7
i=1 → 2 != 7
i=2 → 7 == 7 → return 2


Output:

2

⚠️ Edge Cases

[] → return -1

[5], target = 5 → return 0

Target not present → return -1

Works for unsorted arrays

⏱️ Time & Space Complexity

Time Complexity: O(n)

Space Complexity: O(1)

⭐ One-Line Interview Summary

"Linear search checks each element sequentially and works for unsorted arrays with O(n) time complexity."
