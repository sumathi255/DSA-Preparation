# File: permutations.py

class Solution:
    def permuteDist(self, arr):
        result = []      # to store all permutations
        used = [False] * len(arr)  # to track used elements

        def backtrack(temp):
            # If one permutation is complete
            if len(temp) == len(arr):
                result.append(temp.copy())
                return

            # Try every element
            for i in range(len(arr)):
                if used[i] == False:
                    used[i] = True
                    temp.append(arr[i])

                    backtrack(temp)

                    # Backtrack
                    temp.pop()
                    used[i] = False

        backtrack([])
        return result
