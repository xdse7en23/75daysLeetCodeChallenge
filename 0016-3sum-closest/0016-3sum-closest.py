class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                
                if s < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum
