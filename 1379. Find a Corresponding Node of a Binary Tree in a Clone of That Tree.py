
# Link - https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Space: O(n)
# Time: O(n)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def findNode(head):
            
            if not head:
                return None
            
            if head.val == target.val:
                return head
            
            return findNode(head.left) or findNode(head.right)
        
        return findNode(cloned)