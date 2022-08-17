# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# Time: O(N)
# Space: O(N)

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        @cache
        def getSum(node):

            if not node:
                return 0

            return node.val + getSum(node.left) + getSum(node.right)

        res, total = 0, getSum(root)

        def dfs(node):
            nonlocal res

            if node == None:
                return

            res = max(res, (total - getSum(node)) * getSum(node))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return res % (10**9 + 7)
