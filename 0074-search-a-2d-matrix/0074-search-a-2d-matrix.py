class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            val = matrix[mid // n][mid % n]
            
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False