class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1
            
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
