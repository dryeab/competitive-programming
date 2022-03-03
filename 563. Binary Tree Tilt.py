# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def sum(node):
            if not node: return 0
            node.val += sum(node.left) + sum(node.right)
            return node.val
        sum(root)
        
        def tilt(node):
            
            if not node: return 0
            
            left = node.left.val if node.left else 0
            right = node.right.val if node.right else 0
            
            return abs(left - right) + tilt(node.left) + tilt(node.right)
        
        return tilt(root)