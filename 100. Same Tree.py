
# Link - https://leetcode.com/problems/same-tree/

# Space: O(n)
# Time: O(n)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        if not(p or q):
            return True
        
        if not(p and q):
            return False
        
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)