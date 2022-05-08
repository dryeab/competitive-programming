
# Link - https://leetcode.com/problems/validate-binary-search-tree/

# Space:
# Time:

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def findMax(node):
            if not node:
                return float('-inf')
            return max(node.val, findMax(node.left), findMax(node.right))
        
        def findMin(node):
            if not node:
                return float('inf')
            return min(node.val, findMin(node.left), findMin(node.right))
        
        def validate(node):
            
            if not node: 
                return True
            
            left = findMax(node.left)
            right = findMin(node.right)
            
            if left < node.val < right:
                return validate(node.left) and validate(node.right)
            return False
    
        return validate(root)