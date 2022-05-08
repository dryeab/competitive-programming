
# Link - https://leetcode.com/problems/path-sum-ii/

# Space: O(n)
# Time: O(n ^ 2)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        
        def dfs(root, sum=0):
            
            if not root: return set()
            
            sum += root.val
            
            if not root.left and not root.right: # leaf
                if sum == targetSum:
                    paths.append([root.val])
                    return {len(paths) - 1}
                return set()
            
            left = dfs(root.left, sum)
            right = dfs(root.right, sum)
            
            union = left.union(right)
            
            for i in union:
                paths[i].append(root.val)
            
            return union
        
        
        if root: dfs(root)
        
        return [path[::-1] for path in paths]
                