class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) < 2:
            return s
            
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        c = r = 0
        max_len = max_idx = 0
        
        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
                
            while i - 1 - p[i] >= 0 and i + 1 + p[i] < n and t[i - 1 - p[i]] == t[i + 1 + p[i]]:
                p[i] += 1
                
            if i + p[i] > r:
                c, r = i, i + p[i]
                
            if p[i] > max_len:
                max_len = p[i]
                max_idx = i
                
        start = (max_idx - max_len) // 2
        return s[start : start + max_len]
