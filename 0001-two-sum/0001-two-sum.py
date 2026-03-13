class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}   # value : index
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i