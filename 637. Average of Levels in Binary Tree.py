# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def bfs(root):
            
            ans, q = [], deque([(root, 0)])
            
            while q:
                
                store, level = [], q[0][1]
                
                while q and q[0][1] == level:
                    temp, _ = q.popleft()
                    store.append(temp.val)
                    
                    if temp.left:
                        q.append((temp.left, level+1))
                    if temp.right:
                        q.append((temp.right, level+1))
                
                ans.append(sum(store)/len(store))
            
            return ans
        
        return bfs(root)