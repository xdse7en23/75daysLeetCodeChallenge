class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
            
        start, end = 0, 0
        
        for i in range(len(s)):
            l1, r1 = i, i
            while l1 >= 0 and r1 < len(s) and s[l1] == s[r1]:
                if (r1 - l1) > (end - start):
                    start, end = l1, r1
                l1 -= 1
                r1 += 1
                
            l2, r2 = i, i + 1
            while l2 >= 0 and r2 < len(s) and s[l2] == s[r2]:
                if (r2 - l2) > (end - start):
                    start, end = l2, r2
                l2 -= 1
                r2 += 1
                
        return s[start:end + 1]
