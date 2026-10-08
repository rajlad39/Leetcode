class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        open_count = 0
        
        for char in s:
            if char == '(':
                if open_count > 0:
                    result.append(char)
                open_count += 1
            else:  # char == ')'
                open_count -= 1
                if open_count > 0:
                    result.append(char)
                    
        return "".join(result)