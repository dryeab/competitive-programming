
# Link - https://leetcode.com/problems/longest-univalue-path/

# Space: O(n)
# Time: O(n)

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        ans = 0
        
        def dfs(root):
            nonlocal ans
            
            if not root: return 0
            
            left = dfs(root.left)
            if root.left and root.left.val != root.val:
                left = 0
                
            right = dfs(root.right)
            if root.right and root.right.val != root.val:
                right = 0
            
            ans = max(ans, 1 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        
        return ans - 1