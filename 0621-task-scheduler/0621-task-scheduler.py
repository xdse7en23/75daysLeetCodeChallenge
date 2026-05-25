class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - 65] += 1  
            
        max_freq = max(freq)
    
        max_freq_count = freq.count(max_freq)
        
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(ans, len(tasks))
