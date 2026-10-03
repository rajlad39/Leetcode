class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Base boundary index

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Reset boundary to current index
                    stack.append(i)
                else:
                    # Calculate current valid length
                    max_len = max(max_len, i - stack[-1])

        return max_len