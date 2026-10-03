class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        if i >= n:
            return 0
            
        # 2. Check for optional sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Read digits and build integer
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # Check for 32-bit integer overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            i += 1
            
        return result * sign