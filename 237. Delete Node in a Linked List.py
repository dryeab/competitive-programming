# link - https://leetcode.com/problems/delete-node-in-a-linked-list/

# space: O(n)
# time: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        next = node.next
        
        node.val = next.val
        node.next = next.next
