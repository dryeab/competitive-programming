
# Link - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Space: O(n)
# Time: O(n)

# BFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        q = deque([root] if root else [])
        
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                
                if i != n - 1:
                    node.next = q[0]

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        
        return root