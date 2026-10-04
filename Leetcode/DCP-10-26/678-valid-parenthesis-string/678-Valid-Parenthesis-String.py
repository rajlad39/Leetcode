class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char == ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        # Match remaining '(' with '*' that appear after them
        while open_stack and star_stack:
            if open_stack.pop() > star_stack.pop():
                return False  # '*' appeared before '(' so it cannot match
                
        return len(open_stack) == 0