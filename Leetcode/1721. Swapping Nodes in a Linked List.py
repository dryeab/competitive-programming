
# Link - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Space: O(1)
# Time: O(n)

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        
        node, store = head, []
        for i in range(n):
            if i == k - 1:
                store.append(node)
            if n - k == i:
                store.append(node)
            node = node.next
        
        store[0].val, store[1].val = store[1].val, store[0].val
        
        return head