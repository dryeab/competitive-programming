# link - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# space: O(n)
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        node, store = head, []
        while (node):
            store.append(node.val)
            node = node.next
        
        i, j,ans = 0, len(store) - 1, 0
        while (i < j):
            ans = max(ans, store[i] + store[j])
            i += 1
            j -= 1
        
        return ans
