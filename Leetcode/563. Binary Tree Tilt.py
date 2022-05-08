
# Link - https://leetcode.com/problems/binary-tree-tilt/

# Space: O(n)
# Time: O(n)

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0
        
        def dfs(node):
            
            if not node: return 0
            
            left, right = dfs(node.left), dfs(node.right)
            
            self.answer += abs(right - left)
            
            return node.val + left + right
        
        dfs(root)
        
        return self.answer