# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def serialize(node):
            if not node:
                return "#"
            return "," + str(node.val) + serialize(node.left) + serialize(node.right)
        
        root_str = serialize(root)
        sub_str = serialize(subRoot)
        
        return sub_str in root_str
