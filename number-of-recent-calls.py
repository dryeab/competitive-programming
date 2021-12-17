# link - https://leetcode.com/problems/number-of-recent-calls

class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.requests = []  

    def ping(self, t: int) -> int:
        
        self.requests.append(t)
        
        n = len(self.requests)
        while ((self.counter < n) and (t - self.requests[self.counter] > 3000)):
            self.counter += 1
            
        return len(self.requests[self.counter:])
        
        
