
# Link - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Space: O(1)
# Time: O(log(n))

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        node = root
        
        while node:
            if node.val == val:
                return node
            if node.val > val:
                if not node.left:
                    return None
                node = node.left
            else:
                if not node.right:
                    return None
                node = node.right
