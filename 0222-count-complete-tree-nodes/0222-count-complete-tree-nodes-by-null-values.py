# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def look_for_null(root):
            if not root:
                return 1
            left = look_for_null(root.left)
            right = look_for_null(root.right)
            return left + right
        
        return look_for_null(root) - 1