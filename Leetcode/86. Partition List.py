# link - https://leetcode.com/problems/partition-list/

# space: O(1)
# time: O(n)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head: return head
        
        node, tail, new_head, n = head, None, None, 0
        while node:
            n += 1
            if node.val < x and not new_head:
                new_head = node
            tail = node
            node = node.next
        
        if not new_head: return head
        
        prev, current = None, head
        while n:
            n -= 1
            next = current.next
            if current.val >= x:
                tail.next = current
                if prev:
                    prev.next = current.next
                tail = current
                tail.next = None
            else:
                prev = current
                
            current = next
            
        return new_head
