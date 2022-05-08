
# Link - https://leetcode.com/problems/path-sum/submissions/

# Space: O(n)
# Time: O(n)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sum):
            
            sum += node.val
            
            if not (node.left or node.right):
                return sum == targetSum
            
            return (node.left and dfs(node.left, sum)) or (node.right and dfs(node.right, sum))
        
        return root and dfs(root, 0)