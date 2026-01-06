

2️⃣ Interview Explanation (How to Say)

👉 Interviewer adigite ila cheppali:

"To left rotate the array by one position, I first store the first element in a temporary variable.
Then I shift all elements one position to the left by copying the next element to the current index.
Finally, I place the stored first element at the last position of the array.

This modifies the array in-place without using extra space."

3️⃣ Dry Run (Interview Favorite)

Input:

arr = [1, 2, 3, 4, 5]
n = 5


Steps:

temp = 1
Shift → [2, 3, 4, 5, 5]
Place temp → [2, 3, 4, 5, 1]


Output:

[2, 3, 4, 5, 1]

4️⃣ Edge Cases (Must Mention)

[] → no change

[5] → no change

[1, 2] → [2, 1]

n = 0 or 1 → no rotation

5️⃣ Time & Space Complexity

Time Complexity: O(n)

Space Complexity: O(1)

6️⃣ One-Line Interview Summary

"I rotate the array to the left by one position using a temporary variable and in-place shifting in O(n) time and O(1) space."
