class Solution:
    def checkRedundancy(self, s):
        stack = []

        for ch in s:
            # Push everything except ')'
            if ch != ')':
                stack.append(ch)
            else:
                # When ')' is found, check inside brackets
                top = stack.pop()
                has_operator = False

                # Pop till '('
                while top != '(':
                    if top in ['+', '-', '*', '/']:
                        has_operator = True
                    top = stack.pop()

                # If no operator found → redundant brackets
                if not has_operator:
                    return True

        return False
