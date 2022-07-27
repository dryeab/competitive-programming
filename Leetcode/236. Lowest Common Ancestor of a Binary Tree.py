"""
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        @lru_cache(None)
        def count(root):
            if not root:
                return 0
            return (root.val == q.val or root.val == p.val) + count(root.left) + count(root.right)

        while (True):
            if count(root.left) == 2:
                root = root.left
            elif count(root.right) == 2:
                root = root.right
            else:
                return root
