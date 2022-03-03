# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymmetric(arr):
            i, j = 0, len(arr) - 1
            while i < j:
                if arr[i] != arr[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        
        def bfs(root):
            
            q, d = deque([(root, 0)]), depth(root)
            
            while d:
                
                d -= 1
                store, level = [], q[0][1]
                
                while q and q[0][1] == level:
                    temp, _ = q.popleft()
                    store.append(temp.val if temp else temp)
                    
                    q.append((temp.left if temp else temp, level+1))
                    q.append((temp.right if temp else temp, level+1))
                
                if not isSymmetric(store):
                    return False
            
            return True
        
        return bfs(root)