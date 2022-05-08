
# Link - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Space: O(n)
# Time: O(n)

# BFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        
        q, answer, reverse = deque([root]), [], False
        
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            answer.append(temp if not reverse else temp[::-1])
            reverse = not reverse
        
        return answer



# DFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = []
        
        def dfs(root, depth):
            
            if root:
            
                if depth == len(answer):
                    answer.append([])

                answer[depth].append(root.val)

                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)
        
        dfs(root, 0)
        for i in range(1, len(answer), 2):
            answer[i].reverse()
        
        return answer