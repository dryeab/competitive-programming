# link - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# space: O(1)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while (node and node.next):
            next = node.next
            if node.val == next.val:
                node.next = next.next
            else:
                node = node.next
        return head
