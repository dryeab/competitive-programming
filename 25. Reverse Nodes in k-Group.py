
# link - https://leetcode.com/problems/reverse-nodes-in-k-group/

# space: O(1)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        d = deque()
        
        main = tail = None
        
        node = head
        
        while (node):
            
            # insert the next k nodes to the deque
            i = k
            while (node and i):
                d.append(node)
                node = node.next
                i -= 1
            
            # remove them in reverse order
            while d:
                if not main:
                    main = d.pop() if not i else d.popleft()
                    tail = main
                else:
                    tail.next = d.pop() if not i else d.popleft()
                    tail = tail.next
                    
        tail.next = None       
        return main
