class Solution:
    def removeKdig(self, s, k):
        stack = []

        # Step 1: Use monotonic increasing stack
        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # Step 2: If k still > 0, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # Step 3: Build result and remove leading zeros
        result = ''.join(stack).lstrip('0')

        # Step 4: Handle empty result
        return result if result else "0"
