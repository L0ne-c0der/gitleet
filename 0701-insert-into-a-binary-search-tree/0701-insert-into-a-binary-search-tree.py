# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def _insertIntoBST(root,val):
            if root.val > val:
                if root.left:
                    _insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    _insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        
        _insertIntoBST(root, val)
        return root