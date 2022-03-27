

# Link - https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Space: O(n + m)
# Time: O(n + m)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        store = []
        
        def fetch(node):
            if node:
                store.append(node.val)
                fetch(node.left)
                fetch(node.right)
        
        fetch(root1)
        fetch(root2)
        store.sort()
        
        return store 