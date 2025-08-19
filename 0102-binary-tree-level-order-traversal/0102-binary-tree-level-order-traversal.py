from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #so we use a queue to temp store nodes
        #we use a while loop to iterate till the loop is empty
        #inside, a for loop to run till one level (len(q))
        #from there, we will add each node that we encounter into the resut

        result = []
        q = deque()
        q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        
        return result