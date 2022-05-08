
# Link - https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Space: O(n)
# Time: O(n)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        if not(root.left or root.right):
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))