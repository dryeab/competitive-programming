# link - https://leetcode.com/problems/insertion-sort-list/

# space: O(n)
# time: O(n**2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        
        node, p, prev = head, None, {}
        while (node):
            prev[node] = p
            p = node
            node = node.next
        
        node = head.next
        
        while (node):
            
            current, next, node = node, node.next, prev[node]
            
            while (node and node.val > current.val):
                node = prev[node]
            
            if node != prev[current]:
                if not node: 

                    prev[current].next = next
                    prev[next] = prev[current]

                    current.next = head
                    prev[current] = None
                    prev[head] = current

                    head = current  # change the head pointer
                else:
                    prev[current].next = next
                    prev[next] = prev[current]

                    current.next = node.next
                    prev[node.next] = current

                    node.next = current
                    prev[current] = node
            
            node = next
        return head
