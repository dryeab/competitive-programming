# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Time: O(n)
# Space: O(1)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        while root:
            
            if root.left:
                
                last = root.left
                while last.right:
                    last = last.right
                    
                last.right = root.right
                root.right = root.left
                root.left = None
            
            root = root.right