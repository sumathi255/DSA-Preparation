class Solution:
    def josephus(self, n, k):
        # Step 1: Create list of people
        people = []
        for i in range(1, n + 1):
            people.append(i)

        index = 0

        # Step 2: Remove every k-th person
        while len(people) > 1:
            index = (index + k - 1) % len(people)
            people.pop(index)

        # Step 3: Return the survivor
        return people[0]
