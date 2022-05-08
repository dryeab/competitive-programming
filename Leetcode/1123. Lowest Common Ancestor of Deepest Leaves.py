
# Link - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Space: O(h) : h = findMaxDepth(root)
# Time: O(n)

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        depth = {None: 0} # memo
        def findMaxDepth(node):
            if node not in depth:
                depth[node] = 1 + max(findMaxDepth(node.left), findMaxDepth(node.right))
            return depth[node]
        
        while root:

            ld, rd = findMaxDepth(root.left), findMaxDepth(root.right)
            
            if ld == rd: return root
            
            root = root.left if ld > rd else root.right