
# Link - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Space: O(n)
# Time: O(n)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('-inf')
        
        def dfs(root):
            
            if not root: return 0
            
            left, right = dfs(root.left), dfs(root.right)
            
            self.ans = max(self.ans, root.val + left + right)
            
            res = root.val + max(left, right)
            
            return res if res > 0 else 0
        
        dfs(root)
        
        return self.ans