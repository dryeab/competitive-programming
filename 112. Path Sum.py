# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sumSoFar):
            
            sumSoFar += node.val
            
            if not (node.left or node.right):
                return sumSoFar == targetSum
            
            return (dfs(node.left, sumSoFar) if node.left else False) or \
                        (dfs(node.right, sumSoFar) if node.right else False)
        
        return dfs(root, 0) if root else False