2️⃣ Interview Explanation (MOST IMPORTANT)

👉 Interviewer adigite ila cheppali:

"To rotate the array left by d positions efficiently, I use the reversal algorithm.

The idea is to break the array into two parts:

First d elements

Remaining n-d elements

I reverse both parts individually, and then reverse the entire array.

This results in a left rotation by d positions.

This approach works in-place and does not require extra memory."

3️⃣ Dry Run (Interview Favorite ⭐)

Input:

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2


Steps:

Step 1: Reverse first d elements
[2, 1, 3, 4, 5, 6, 7]

Step 2: Reverse remaining elements
[2, 1, 7, 6, 5, 4, 3]

Step 3: Reverse entire array
[3, 4, 5, 6, 7, 1, 2]


✅ Left rotated by 2 positions

4️⃣ Edge Cases (Must Mention in Interview)

arr = [] → return []

arr = [5] → unchanged

d = 0 → unchanged

d = n → unchanged

d > n → handled using d = d % n

5️⃣ Time & Space Complexity (Say Confidently)

Time Complexity: O(n)

Space Complexity: O(1) (in-place)
Why Reversal Algorithm? (Follow-up Question)

Q: Why not shift elements one by one d times?
A:

That approach takes O(n*d) time, which is inefficient for large d.
The reversal algorithm achieves the same result in O(n) time.

7️⃣ One-Line Interview Summary (Very Important ⭐)

"I used the reversal algorithm to rotate the array left by d positions in O(n) time and O(1) space."
