
# Link - https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Space: O(n)

class FindElements:

    def __init__(self, root: Optional[TreeNode]): # O(n)
        
        self.store = set()
        root.val = 0
        
        self.validate(root)
    
    def validate(self, node): # O(n)
        
        self.store.add(node.val)
        
        if node.left:
            node.left.val = 2*node.val + 1
            self.validate(node.left)
        
        if node.right:
            node.right.val = 2*node.val + 2
            self.validate(node.right)

    def find(self, target: int) -> bool: # O(n)
        return target in self.store