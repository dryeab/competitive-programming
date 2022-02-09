
# link - https://leetcode.com/problems/intersection-of-two-linked-lists/

# space: O(1)
# time: O(m+n)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2, round1, round2 = headA, headB, 1, 1
        while (round1 < 3 and round2 < 3):
            if p1 == p2:
                return p1
            
            # change p1
            if p1.next == None:
                round1 += 1
                p1 = headB
            else:
                p1 = p1.next
            
            # change p2
            if p2.next == None:
                round2 += 1
                p2 = headA
            else:
                p2 = p2.next
        
        return None
      

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
        
