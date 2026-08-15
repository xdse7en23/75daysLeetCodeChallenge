class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        temp = x
        reversed_num = 0
        
        while temp > 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp //= 10
            
        return x == reversed_num

