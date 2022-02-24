
# link - https://leetcode.com/problems/merge-k-sorted-lists/

# Solution 1
    # Space: O(n)
    # Time: O(n*log(n))

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


    
# Solution 2
    # Space: O(k)
    # Time: O(n*log(k))

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        
        heapq.heapify(heap)
        
        sentinel = ListNode()
        node = sentinel
        
        while heap:
            val = heapq.heappop(heap)
            node.next = val[2]
            node = node.next
                             
            if node.next:
                next = node.next
                heapq.heappush(heap, (next.val, val[1], next))
        
        return sentinel.next
