# link - https://leetcode.com/problems/middle-of-the-linked-list/

# space: O(1)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slow = slow.next
        return slow
