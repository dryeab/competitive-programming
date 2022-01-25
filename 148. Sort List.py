# link - https://leetcode.com/problems/sort-list/

# space: O(1)
# time: O(nlog(n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# merge two sorted lists
def merge(head1, head2):

    head = tail = None
    while (head1 or head2):

        if head1 and (not head2 or (head1.val <= head2.val)):
            if tail:
                tail.next = head1
            else:
                head = head1
            tail = head1
            head1 = head1.next

        if head2 and (not head1 or (head2.val < head1.val)):
            if tail:
                tail.next = head2
            else:
                head = tail = head2
            tail = head2
            head2 = head2.next
    
        tail.next = None

    return head

# sort n-sized list
def sort(head, n):
    
    if n < 2: return head

    i, node = 1, head
    while (i < n//2):
        node = node.next
        i += 1
        
    next = node.next
    node.next = None
    
    return merge(sort(head, n//2), sort(next, n-n//2))

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        n, node = 0, head
        while (node):
            n += 1
            node = node.next
        
        return sort(head, n)
