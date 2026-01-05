Edge Cases (Must Mention in Interview)

Empty array → [] → True

Single element → [5] → True

Already sorted → [1, 2, 3, 4] → True

Not sorted → [1, 3, 2] → False

All equal elements → [2, 2, 2] → True

Negative numbers → [-5, -3, -1] → True

Interview Explanation (Step by Step – Beginner Friendly)

--->>> Interviewer adigite ila cheppali:

"To check whether an array is sorted, I compare every element with its next element.
If at any point the current element is greater than the next element, it means the array is not sorted, so I return False immediately.

If the loop completes without finding such a case, the array is sorted and I return True.

I also handle edge cases:

An empty array or a single element array is always considered sorted."

5️⃣ Time & Space Complexity 

Time Complexity: O(n)

Space Complexity: O(1)

6️⃣ Dry Run Example (Interview Favorite)

Input:

arr = [1, 3, 2]


Steps:

Compare 1 and 3 → OK

Compare 3 and 2 → 3 > 2 ❌

Return False
