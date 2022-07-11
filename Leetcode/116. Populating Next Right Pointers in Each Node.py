"""
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    Time: O(n)
    Space: O(1)
    
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        start = root

        while start:

            cur, start = start, start.left

            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next

        return root
