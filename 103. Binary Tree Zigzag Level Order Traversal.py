# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            
            ans, q, fromLeft = [], deque(), True
            
            if root: q.append((root, 0))
                
            while q:

                store, level = [], q[0][1]
                
                while q and q[0][1] == level:
                    temp, _ = q.popleft()
                    store.append(temp.val)
                    
                    if temp.left:
                        q.append((temp.left, level+1))
                    if temp.right:
                        q.append((temp.right, level+1))
                
                if not fromLeft:
                    store.reverse()
                
                ans.append(store)
                
                fromLeft = not fromLeft
            
            return ans
        
        return bfs(root)