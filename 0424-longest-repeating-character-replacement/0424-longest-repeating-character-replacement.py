class Solution(object):
    def characterReplacement(self, s, k):
        count = [0] * 26
        left = 0
        max_freq = 0
        res = 0
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            
            if count[idx] > max_freq:
                max_freq = count[idx]
            
            if (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res