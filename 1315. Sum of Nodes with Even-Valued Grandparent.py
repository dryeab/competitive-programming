# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        count = 0
        
        if root.val % 2 == 0:
            
            if root.left:
                count += root.left.left.val if root.left.left else 0
                count += root.left.right.val if root.left.right else 0
            if root.right:
                count += root.right.left.val if root.right.left else 0
                count += root.right.right.val if root.right.right else 0
        
        return count + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)