# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def _maxDepth(node, count):
            if not node:
                return count
            count+=1
            return max(_maxDepth(node.left, count), _maxDepth(node.right,count))
        
        return _maxDepth(root, 0)