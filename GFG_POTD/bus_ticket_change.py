class Solution:
    def busTicketChange(self, arr):
        five = 0
        ten = 0

        for note in arr:
            if note == 5:
                # No change needed
                five += 1

            elif note == 10:
                # Need to give 5 as change
                if five == 0:
                    return False
                five -= 1
                ten += 1

            else:  # note == 20
                # Prefer giving 10 + 5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # Else give three 5s
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True


# Example usage
if __name__ == "__main__":
    arr = [5, 5, 5, 10, 20]
    print(Solution().busTicketChange(arr))
