# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def _postOrderTraversal(root, arr):
            if not root:
                return
            _postOrderTraversal(root.left, arr)
            _postOrderTraversal(root.right, arr)
            arr.append(root.val)
            return
        _postOrderTraversal(root, result)
        return result