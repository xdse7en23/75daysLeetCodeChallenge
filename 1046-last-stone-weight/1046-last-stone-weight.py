import bisect

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
     
        stones.sort()
        
        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 != stone2:
                diff = stone1 - stone2
                
                bisect.insort(stones, diff)
                
        return stones[0] if stones else 0
