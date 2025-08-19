import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #creating a new copy
        copied_tree = copy.deepcopy(root) #for shallow, copy.copy
        
        def reverseTree(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp 
            reverseTree(node.left)
            reverseTree(node.right)
            return
        
        reverseTree(copied_tree)

        def compareTree(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return compareTree(root1.left, root2.left) and compareTree(root1.right, root2.right)
            return False

        return compareTree(root, copied_tree)

