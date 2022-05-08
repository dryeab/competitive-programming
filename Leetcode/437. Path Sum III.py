
# Link - https://leetcode.com/problems/path-sum-iii/

# Space: O(n)
# Time: O(n)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ans, cache = 0, Counter()
        cache[0] = 1

        def dfs(root, pathSum):

            nonlocal ans

            if not root:
                return

            pathSum += root.val

            ans += cache[pathSum - targetSum]

            cache[pathSum] += 1

            dfs(root.left, pathSum)
            dfs(root.right, pathSum)

            cache[pathSum] -= 1  # backtrack

        dfs(root, 0)

        return ans

# Space: O(n ^ 2)
# Time: O(n ^ 2)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ans = 0

        def dfs(root, pathSum):
            nonlocal ans

            if not root:
                return

            newPathSum = [x + root.val for x in pathSum]
            newPathSum.append(root.val)

            ans += sum(targetSum == x for x in newPathSum)

            dfs(root.left, newPathSum)
            dfs(root.right, newPathSum)

        dfs(root, [])

        return ans
