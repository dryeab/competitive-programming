
# Link - https://leetcode.com/problems/deepest-leaves-sum/

# Space: O(n)
# Time: O(n)

# BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        while q:

            sum = 0

            for _ in range(len(q)):
                node = q.popleft()
                sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return sum

# DFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        sum, level = -1, -1
        
        def dfs(node, l):
            nonlocal sum, level
            
            if not node: return
            
            if level == l:
                sum += node.val
            if l > level:
                sum = node.val
                level = l
            
            dfs(node.left, l + 1)
            dfs(node.right, l + 1)
        
        dfs(root, 0)
        
        return sum