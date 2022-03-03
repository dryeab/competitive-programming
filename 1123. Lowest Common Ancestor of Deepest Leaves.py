# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def findMaxDepth(node):
            if not node:
                return 0
            return 1 + max(findMaxDepth(node.left), findMaxDepth(node.right))
        
        node = root
        
        while node:
            
            left, right = findMaxDepth(node.left), findMaxDepth(node.right)
            
            if left == right:
                return node
            
            if left > right:
                node = node.left
            else:
                node = node.right