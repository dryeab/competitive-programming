# link - https://leetcode.com/problems/next-greater-node-in-linked-list/

# space: O(n)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        node, store = head, []
        while (node):
            store.append(node.val)
            node = node.next
            
        answer  = [0] * len(store)
        mono_stack = []
        
        for i in range(len(store)):
            while mono_stack and store[i] > store[mono_stack[-1]]:
                answer[mono_stack.pop()] = store[i]
            mono_stack.append(i)
        
        return answer
