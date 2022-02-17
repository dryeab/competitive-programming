
# link - https://leetcode.com/problems/merge-k-sorted-lists/


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
