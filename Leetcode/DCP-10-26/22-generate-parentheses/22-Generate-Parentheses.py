class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_N, close_N, current_str):
            if open_N == n and close_N == n:
                res.append(current_str)
                return
            
            if open_N < n:
                backtrack(open_N + 1, close_N, current_str + "(")
                
            if close_N < open_N:
                backtrack(open_N, close_N + 1, current_str + ")")
        
        backtrack(0, 0, "")
        return res