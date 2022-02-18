
# link - https://leetcode.com/problems/find-k-closest-elements/

# space: O(k)
# time: O(n)

def isCloser(a, b, x):
    if (abs(a-x) < abs(b-x)) or (abs(a-x) == abs(b-x) and a < b):
        return True
    return False

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        store = deque()
        
        for num in arr:
            if len(store) == k and isCloser(num, store[0], x):
                store.popleft()
                store.append(num)
            elif len(store) < k:
                store.append(num)
                
        return list(store)
