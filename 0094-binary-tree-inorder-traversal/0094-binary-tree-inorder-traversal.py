# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def _inorderTraversal(root, arr):
            if not root:
                return
            _inorderTraversal(root.left, arr)
            arr.append(root.val)
            _inorderTraversal(root.right, arr)

        _inorderTraversal(root, result)
        return result
