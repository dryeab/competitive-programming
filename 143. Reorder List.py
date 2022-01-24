# link - https://leetcode.com/problems/reorder-list/

# space: O(n)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        node, store = head, []
        while (node):
            store.append(node)
            node = node.next
        
        i, j = 1, len(store) - 1
        tail = head
        while (i <= j):
            store[j].next = store[i]
            tail.next = store[j]
            tail = store[i]
            
            i += 1
            j -= 1
            
        tail.next = None
            
            
        
