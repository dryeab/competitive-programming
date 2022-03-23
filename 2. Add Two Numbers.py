
# Link - https://leetcode.com/problems/add-two-numbers/

# Space: O(n)
# Time: O(max(len(l1), len(l2)))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = tail = ListNode()
        carry = 0
        
        while l1 or l2 or carry:
            
            res = carry
            
            if l1:
                res += l1.val
                l1 = l1.next
                
            if l2:
                res += l2.val
                l2 = l2.next
            
            res, carry = res % 10, res//10
            tail.next = ListNode(res)
            tail = tail.next
        
        return dummy.next