from typing import List

class Solution:
    def leaders(self, arr: List[int]) -> List[int]:
        """
        A leader is an element which is greater than or equal to
        all the elements to its right side.
        """

        n = len(arr)
        leaders = []

        # Last element is always a leader
        max_from_right = arr[-1]
        leaders.append(max_from_right)

        # Traverse array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders.append(arr[i])

        # Reverse to maintain original order
        leaders.reverse()
        return leaders


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print("Leaders:", Solution().leaders(arr))
