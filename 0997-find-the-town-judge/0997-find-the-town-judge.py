class Solution(object):
    def findJudge(self, n, trust):
        trust_scores = [0] * (n + 1)
        
        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1
            
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1
