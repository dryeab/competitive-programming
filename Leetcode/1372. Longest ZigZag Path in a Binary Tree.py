# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Time: O(N)
# Space: O(H)

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

            if not root:
                return [-1, -1, 0]

            left, right = dfs(root.left), dfs(root.right)

            return [
                right[1] + 1,
                left[0] + 1,
                max(left[2], right[2], right[1] + 1, left[0] + 1)
            ]

        return dfs(root)[2]
