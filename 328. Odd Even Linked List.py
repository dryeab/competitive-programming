
# Link - https://leetcode.com/problems/odd-even-linked-list/

# Space: O(1)
# Time: O(n)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 0, 1, 2 elements
        if not head or not head.next or not head.next.next:
            return head
        
        lists = odd, even = [head, head.next]
        
        while (odd.next and odd.next.next) or (even.next and even.next.next):
            
            if odd.next and odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            
            if even.next and even.next.next:
                even.next = even.next.next
                even = even.next
        
        even.next, odd.next = None, lists[1]
        
        return lists[0]