
# link - https://leetcode.com/problems/merge-k-sorted-lists/

# solution 1

# space: O(n)
# time: O(nlog(n))

import heapq

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

    
# solution 2

def counter(lists):
    count = {}
    for list in lists:
        
        while list:
            if list.val in count:
                count[list.val] += 1
            else:
                count[list.val] = 1
            list = list.next
            
    return count

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = tail = None
        
        count = counter(lists)
        
        for i in range(-10**4, 10**4+1):
            while count.get(i, 0):
                if head == None:
                    head = tail = ListNode(i)
                else:
                    tail.next = ListNode(i)
                    tail = tail.next
                    
                count[i] -= 1
        
        return head
