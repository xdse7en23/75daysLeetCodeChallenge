class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_map = {0: 1}
        current_sum = 0
        count = 0
        
        get_count = prefix_map.get
        
        for num in nums:
            current_sum += num
            
            diff = current_sum - k
            if diff in prefix_map:
                count += prefix_map[diff]
                
            prefix_map[current_sum] = get_count(current_sum, 0) + 1
            
        return count
