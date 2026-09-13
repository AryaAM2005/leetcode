class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case: dividing by 1 returns the dividend itself
        if divisor == 1:
            return dividend
      
        # Handle overflow case: INT_MIN / -1 would overflow, return INT_MAX
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
      
        # Determine if result should be positive (same signs) or negative (different signs)
        is_positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
      
        # Convert both numbers to negative to avoid overflow issues
        # (negative range is larger than positive range in 32-bit integers)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
      
        # Perform division using bit manipulation and subtraction
        quotient = 0
        while dividend <= divisor:  # Both are negative, so <= means abs(dividend) >= abs(divisor)
            # Find the largest multiple of divisor that can be subtracted from dividend
            current_divisor = divisor
            current_quotient = 1
          
            # Double the divisor using left shift until it exceeds dividend
            # Check >= -(2^30) to prevent overflow when shifting
            while current_divisor >= -(2**30) and dividend <= (current_divisor << 1):
                current_divisor <<= 1  # Multiply by 2
                current_quotient <<= 1  # Multiply by 2
          
            # Subtract the largest found multiple from dividend
            dividend -= current_divisor
            quotient += current_quotient
      
        # Apply the correct sign to the result
        return quotient if is_positive else -quotient
