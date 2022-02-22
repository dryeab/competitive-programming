
# link - https://leetcode.com/problems/merge-k-sorted-lists/

# solution 1

# space: O(n)
# time: O(nlog(n))

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ans = []
        
        for lst in lists:
            while lst:
                heapq.heappush(ans, lst.val)
                lst = lst.next
        
        head = tail = None
        
        while ans:
            node = ListNode(heapq.heappop(ans))
            if head == None:
                head = tail = node
            else:
                tail.next = node
                tail = node
            
        return head
