
# Link - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Space: O(n)
# Time: O(n)

# DFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        if root.children:
            return 1 + max(self.maxDepth(child) for child in root.children)
        
        return 1

# BFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        answer, q = 0, deque([root] if root else [])
        
        while q:
            
            answer += 1
            
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)

        return answer