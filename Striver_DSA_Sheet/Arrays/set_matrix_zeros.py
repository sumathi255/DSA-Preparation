from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the input matrix in-place such that if an element
        is 0, set its entire row and column to 0.
        """

        n = len(matrix)
        m = len(matrix[0])
        col0 = 1  # Flag to track if first column should be zeroed

        # Step 1: Use first row and first column as markers
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row
                    if j != 0:
                        matrix[0][j] = 0  # mark column
                    else:
                        col0 = 0  # first column needs to be zeroed

        # Step 2: Iterate through the matrix using markers
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix  # optional, since modification is in-place


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    mat = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Matrix after setZeroes:")
    print(Solution().setZeroes(mat))
