
# link - https://leetcode.com/problems/rotate-list/

# space: O(1)
# time: O(n)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not(head and head.next and k):
            return head
        
        n, node = 0, head # count the number of nodes
        while (node):
            n += 1
            if node.next == None: # save the tail
                tail = node
            node = node.next
            
        k %= n
        
        if not(k):
            return head
        
        i, node = 0, head # counter
        while i + 1 < n - k:
            node = node.next
            i += 1
        
        old_head = head
        
        head = node.next
        tail.next = old_head
        node.next = None
        
        return head
