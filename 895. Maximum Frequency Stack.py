
# Link - https://leetcode.com/problems/maximum-frequency-stack/

# Space: O(n) : n = self.no
# Time:
    # __init__: O(1)
    # push: O(log(n))
    # pop: O(log(n))

class FreqStack:

    def __init__(self):
        
        self.freq = Counter()
        self.heap = []
        self.no = 0 # number of times push is called

    def push(self, val: int) -> None:
        
        self.freq[val] += 1
        self.no += 1
        
        heapq.heappush(self.heap, (-self.freq[val], -self.no, val))

    def pop(self) -> int:
        
        val = heapq.heappop(self.heap)[2]
        self.freq[val] -= 1
        
        return val