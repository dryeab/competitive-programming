# link - https://leetcode.com/problems/remove-linked-list-elements/

# space: O(1)
# time: O(n)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
