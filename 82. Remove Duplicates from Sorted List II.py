
# Link - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Space: O(n)
# Time: O(n)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = tail = ListNode()
        node = next = head
        
        while node:
            
            while next and node.val == next.val:
                next = next.next
                
            if next == node.next:
                tail.next = node
                tail = tail.next
                
            node = next
        
        tail.next = None
        
        return dummy.next