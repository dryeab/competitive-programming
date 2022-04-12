
# Link - https://leetcode.com/problems/house-robber-iii/

# Space: O(n)
# Time: O(n)

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {None: 0}
        
        def dp(node):
            
            if node not in memo:

                robbed = node.val
                if node.left:
                    robbed += dp(node.left.left) + dp(node.left.right)
                if node.right:
                    robbed += dp(node.right.left) + dp(node.right.right)

                not_robbed = dp(node.left) + dp(node.right)

                memo[node] = max(robbed, not_robbed)
            
            return memo[node]
        
        return dp(root)