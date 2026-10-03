class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1  # 2147483647
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying by 10
            if rev > MAX_INT // 10 or (rev == MAX_INT // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return rev * sign