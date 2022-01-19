# link  - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# space: O(n)
# time: O(n)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        store = []
        
        while (head):
            store.append(head.val)
            head = head.next
        
        i, j = 0, len(store) - 1
        while (i < j):
            if store[i] != store[j]:
                return False
            i += 1
            j -= 1
            
        return True      
