
# Link - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Space: ~
# Time: O(n)

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []

        if not root:
            return answer

        q = deque([root])

        while q:

            M = float('-inf')

            for _ in range(len(q)):
                
                node = q.popleft()
                M = max(M, node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)

            answer.append(M)

        return answer