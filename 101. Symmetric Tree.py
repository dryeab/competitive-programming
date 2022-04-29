
# Link - https://leetcode.com/problems/symmetric-tree/

# Space: O(n)
# Time: O(n)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(left, right):
            if not (left or right): # both are none
                return True
            if not (left and right): # one of them is none
                return False
            
            return left.val == right.val and symmetric(left.left, right.right) \
                and symmetric(left.right, right.left)
        
        return symmetric(root.left, root.right)

# BFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        
        while q:
            
            store, count = [], 0
            for _ in range(len(q)):
                
                node = q.popleft()
                if node: count += 1 # count of not null values
                    
                store.append(node.val if node else node)
                
                q.append(node.left if node else node)
                q.append(node.right if node else node)
            
            if count == 0: return True
            if store != store[::-1]: return False

