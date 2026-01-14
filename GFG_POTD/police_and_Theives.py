class Solution:
    def catchThieves(self, arr, k):
        police = []
        thieves = []

        # Store positions of police and thieves
        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            else:
                thieves.append(i)

        i = 0  # pointer for police
        j = 0  # pointer for thieves
        count = 0

        # Two pointer approach
        while i < len(police) and j < len(thieves):
            if abs(police[i] - thieves[j]) <= k:
                count += 1
                i += 1
                j += 1
            elif police[i] < thieves[j]:
                i += 1
            else:
                j += 1

        return count


# Example usage
if __name__ == "__main__":
    arr = ['P', 'T', 'T', 'P', 'T']
    k = 1
    print(Solution().catchThieves(arr, k))
