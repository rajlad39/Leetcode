class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: valid combination of length 2 * n reached
            if len(current_str) == 2 * n:
                res.append(current_str)
                return

            # Branch 1: Add open parenthesis if limit not reached
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")

            # Branch 2: Add close parenthesis if open count > close count
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")

        backtrack(0, 0, "")
        return res