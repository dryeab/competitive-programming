
# Link - https://leetcode.com/problems/maximum-binary-tree/

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def getNode(i, j):
            
            if i == j:
                return None
            
            if j == i + 1:
                return TreeNode(nums[i])
            
            k = max([x for x in range(i, j)], key=lambda x: nums[x])

            return TreeNode(
                val = nums[k],
                left = getNode(i, k),
                right = getNode(k+1, j)
            )
        
        return getNode(0, len(nums))