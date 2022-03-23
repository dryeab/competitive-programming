
# Link - https://leetcode.com/problems/copy-list-with-random-pointer/

# Space: O(n)
# Time: O(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return head
        
        index, answer = {}, []
        node, i = head, 0
        
        while node:
           
            index[node] = i
            answer.append(Node(node.val))
            
            node = node.next
            i += 1
        
        node = head
        for j in range(len(answer)):
            
            if j + 1 < len(answer):
                answer[j].next = answer[j+1]
            
            if node.random != None:
                answer[j].random = answer[index[node.random]]
            
            node = node.next
        
        return answer[0]
        