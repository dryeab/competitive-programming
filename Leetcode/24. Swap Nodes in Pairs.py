# link - https://leetcode.com/problems/swap-nodes-in-pairs/

# space: O(1)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
 
        node = head
        while (node and node.next):
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        
        return head
                
            
