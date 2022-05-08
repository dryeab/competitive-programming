
# Link - https://leetcode.com/problems/find-median-from-data-stream/

# Space: O(n)

# Time:
    # __init__ : O(1)
    # addNum: O(log(n))
    # findMedian: O(1)

class MedianFinder:

    def __init__(self):
        self.min = [] # max-heap
        self.max = [] # min-heap

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.min, -num)
        
        while len(self.min) > (len(self.min) + len(self.max))//2:
            heapq.heappush(self.max, -heapq.heappop(self.min))
        
        while self.min and -self.min[0] > self.max[0]:
            heapq.heappush(self.max, -heapq.heappop(self.min))
            heapq.heappush(self.min, -heapq.heappop(self.max))

    def findMedian(self) -> float:
        
        n = len(self.min) + len(self.max)
        
        if n % 2:
            return self.max[0]
        else:
            return (-self.min[0] + self.max[0])/2
