# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def findMax(node): # node != None
            
            if not(node.left or node.right): # no child
                return node
            
            max = node
            
            if node.left:
                left = findMax(node.left)
                if left.val > max.val:
                    max = left
            
            if node.right:
                right = findMax(node.right)
                if right.val > max.val:
                    max = right
            
            return max
        
        def findMin(node): # node != None
            
            if not(node.left or node.right):
                return node
            
            min = node
            
            if node.left:
                left = findMin(node.left)
                if left.val < min.val:
                    min = left
            
            if node.right:
                right = findMin(node.right)
                if right.val < min.val:
                    min = right
            
            return min
        
        def validate(node):
            
            if node.left or node.right:
                
                left = findMax(node.left) if node.left else TreeNode(float('-inf'))
                right = findMin(node.right) if node.right else TreeNode(float('inf'))
                
                if not(left.val < node.val < right.val):
                    left.val, node.val, right.val = sorted([left.val, node.val, right.val])
                else:
                    if node.left:
                        validate(node.left)
                    if node.right:
                        validate(node.right)

        validate(root)