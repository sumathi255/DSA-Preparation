Interview Explanation (MOST IMPORTANT)

👉 Interviewer adigite ila explain cheyyali:

"I use two pointers.
Pointer i traverses the array, and pointer j keeps track of the position where the next non-zero element should be placed.

Whenever I find a non-zero element, I swap it with the element at index j and increment j.

By the end, all non-zero elements are moved to the front in the same order, and all zeros are shifted to the end.

The operation is done in-place without using extra space."

5️⃣ Dry Run (Interview Favorite ⭐)

Input:

nums = [0, 1, 0, 3, 12]


Steps:

i=0 → nums[i]=0 → skip
i=1 → nums[i]=1 → swap with nums[j]
      [1, 0, 0, 3, 12], j=1
i=2 → nums[i]=0 → skip
i=3 → nums[i]=3 → swap
      [1, 3, 0, 0, 12], j=2
i=4 → nums[i]=12 → swap
      [1, 3, 12, 0, 0], j=3


✅ Final output:

[1, 3, 12, 0, 0]

6️⃣ Edge Cases (Must Mention)

[] → unchanged

[0, 0, 0] → unchanged

[1, 2, 3] → unchanged

[0, 1] → [1, 0]

Single element

7️⃣ Time & Space Complexity (Say Confidently)

Time Complexity: O(n)

Space Complexity: O(1)

8️⃣ Follow-up Interview Questions & Answers
Q1️⃣ Why swapping instead of creating new array?

Answer:

To satisfy the in-place constraint and avoid extra memory.

Q2️⃣ Does this preserve order?

Answer:

Yes, the relative order of non-zero elements is preserved.

Q3️⃣ Alternative approach?

Answer:

Count non-zero elements and overwrite array, but this method is cleaner.

⭐ One-Line Interview Summary

"I used a two-pointer in-place approach to move all zeros to the end while maintaining the order of non-zero elements."
