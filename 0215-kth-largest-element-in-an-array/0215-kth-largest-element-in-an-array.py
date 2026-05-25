class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MIN_VAL = -10000
        MAX_VAL = 10000
        
        count_bucket = [0] * (MAX_VAL - MIN_VAL + 1)
        
        for num in nums:
            count_bucket[num - MIN_VAL] += 1
        
        for i in range(len(count_bucket) - 1, -1, -1):
            k -= count_bucket[i]
            if k <= 0:
                return i + MIN_VAL
