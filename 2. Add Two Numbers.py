

# link - https://leetcode.com/problems/add-two-numbers/

# space: O(n)
# time: O(max(n, m))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry, head, tail = 0, None, None

        while (l1 or l2 or carry):

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry

            carry = sum // 10
            sum = sum % 10

            node = ListNode(sum)

            if not head:
                head = node
                tail = head
            else:
                tail.next = node
                tail = tail.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return head
