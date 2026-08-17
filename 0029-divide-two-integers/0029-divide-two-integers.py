class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        n, d = abs(dividend), abs(divisor)
        quotient = 0
        
        while n >= d:
            temp_d, count = d, 1
            while n >= (temp_d << 1):
                temp_d <<= 1
                count <<= 1
            
            n -= temp_d
            quotient += count
        result = -quotient if is_negative else quotient
        return max(MIN_INT, min(MAX_INT, result))
