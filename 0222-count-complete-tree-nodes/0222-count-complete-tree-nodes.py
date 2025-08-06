# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def _countNodes(root, count):
            if not root:
                return count
            count+=1 + _countNodes(root.left,count) + _countNodes(root.right,count)
            return count
        totalCount = _countNodes(root, 0)
        return totalCount
