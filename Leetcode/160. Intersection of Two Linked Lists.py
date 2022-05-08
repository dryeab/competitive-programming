
# link - https://leetcode.com/problems/intersection-of-two-linked-lists/

# space: O(1)
# time: O(m+n)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while (p1 != p2):
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
      

# space: O(m+n)
# time: O(max(m, n))

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        p1, p2, store = headA, headB, set()
        
        while p1 or p2:

            if p1 and p1 in store:
                return p1
            store.add(p1)
            
            if p2 and p2 in store:
                return p2
            store.add(p2)
            
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        return None
        
