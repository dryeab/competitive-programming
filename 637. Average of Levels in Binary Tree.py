
# Link - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Space: O(n)
# Time: O(n)

# BFS
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q, answer = deque([root]), []
        while q:
            n, sum = len(q), 0
            for _ in range(n):
                node = q.popleft()
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            answer.append(sum/n)
        
        return answer


# Space: O(n)
# Time: O(h)

# DFS
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        sum, num, maxDepth = defaultdict(int), defaultdict(int), 0
        
        def dfs(node, depth):
            nonlocal maxDepth
            maxDepth = max(depth, maxDepth)
            
            if node:
                sum[depth] += node.val
                num[depth] += 1
                
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        return [sum[i]/num[i] for i in range(maxDepth)]