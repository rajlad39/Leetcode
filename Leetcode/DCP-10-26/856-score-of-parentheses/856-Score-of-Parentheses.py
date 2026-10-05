class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Tracks scores at each level

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                inner_score = stack.pop()
                # If inner_score is 0, it was "()", so score is 1.
                # Otherwise, it was "(A)", so score is 2 * A.
                stack[-1] += max(2 * inner_score, 1)

        return stack[0]