# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        vot = defaultdict(list)
        
        q = deque([(root, 0)])
        
        while q:
            cvot = defaultdict(list)
            for _ in range(len(q)):
                node, col = q.popleft()
                cvot[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
            for col in cvot:
                vot[col].extend(sorted(cvot[col]))
        
        return [vot[col] for col in sorted(vot)]