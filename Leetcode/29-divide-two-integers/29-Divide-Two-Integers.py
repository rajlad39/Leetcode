class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer boundaries
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Handle 32-bit overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        is_negative = (dividend < 0) ^ (divisor < 0)

        # Convert to absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Perform bitwise division
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            
            # Double temp_divisor using left shift until it exceeds dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1

            dividend -= temp_divisor
            quotient += count

        # Apply sign and clamp result to 32-bit range
        res = -quotient if is_negative else quotient
        return max(MIN_INT, min(MAX_INT, res))