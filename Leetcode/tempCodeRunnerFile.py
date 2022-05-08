"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        M = 0
        if root.children:
            for child in root.children:
                M = max(M, self.maxDepth(child))
        return 1 + M