# link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# space: O(n)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        store, node = [], head
        
        while (node):
            store.append(node)
            node = node.next
            
        if n == len(store):
            if len(store) == 1:
                return None
            return store[1]
        
        store[-(n+1)].next = store[-n].next
        
        return store[0]
        
        
