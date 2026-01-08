from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise in-place.
        Steps:
        1. Transpose the matrix
        2. Reverse each row
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    Solution().rotate(mat)
    print("Rotated Matrix:")
    for row in mat:
        print(row)
