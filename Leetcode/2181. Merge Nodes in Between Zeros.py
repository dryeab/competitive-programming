
# link - https://leetcode.com/problems/merge-nodes-in-between-zeros/

# space: O(1)
# time: O(n)

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum, cur, node = 0, head, head.next
        while node:
            if node.val == 0:
                cur.val = sum
                if not node.next:
                    cur.next = None
                cur = cur.next
                sum = 0
            sum += node.val
            node = node.next
        return head
