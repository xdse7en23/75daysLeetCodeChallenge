class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum / float(k)