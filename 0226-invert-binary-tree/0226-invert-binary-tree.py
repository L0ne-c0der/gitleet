# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invertTree(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            _invertTree(node.left)
            _invertTree(node.right)
            return
        _invertTree(root)
        return root