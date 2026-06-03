class Solution(object):
    def fib(self, n):
        if n < 2:
            return n
            
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
            
        return prev1
