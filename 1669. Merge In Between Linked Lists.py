
# Link - https://leetcode.com/problems/merge-in-between-linked-lists/

# Space: O(1)
# Time: O(m + b) -:> m:list2.length

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # get the tail of the second list
        node = list2
        while node:
            list2_tail = node
            node = node.next
            
        node = list1
        for i in range(b+1):
            if i == a - 1:
                node.next, node = list2, node.next
            else:
                node = node.next
            
        list2_tail.next = node
            
        return list1