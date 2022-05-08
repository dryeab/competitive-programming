
# link - https://leetcode.com/problems/linked-list-cycle/

# space: O(n)
# time: O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = set()
        while head:
            if head in store:
                return True
            store.add(head)    
            head = head.next
        return False


# space: O(1)
# time: -

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while (slow != fast):
            if not fast: return False
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        return True
