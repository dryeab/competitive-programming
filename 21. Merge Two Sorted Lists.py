# link - https://leetcode.com/problems/merge-two-sorted-lists/

# space: O(1)
# time: O(n+m) : n, m - length of list 1 and 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # set the head the first time
        head = None
        if list1:
            if not list2:
                head = list1
            elif list1.val < list2.val:
                head = list1
            
            if head:
                list1 = list1.next
        if not head and list2:
            head = list2
            list2 = list2.next
        
        tail = head
            
        while (list1 or list2):
            if list1:
                if not list2:
                    tail.next = list1
                    list1 = list1.next
                elif list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
            
        return head   
