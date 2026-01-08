from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return all elements of the matrix in spiral order.
        """
        ans = []

        # Define boundaries
        n = len(matrix)
        m = len(matrix[0])
        top, left = 0, 0
        bottom, right = n - 1, m - 1

        while top <= bottom and left <= right:
            # Traverse top row from left to right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse right column from top to bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Traverse bottom row from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Traverse left column from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    result = Solution().spiralOrder(mat)
    print("Spiral Order:", result)
