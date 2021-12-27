
# link - https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        store = deque()
        i = 0
        
        for val in pushed:
            
            store.append(val)
            
            while i < len(popped) and len(store) and store[-1] == popped[i]:
                store.pop()
                i += 1
        
        return len(store) == 0
            
                
            
            
