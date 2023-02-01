class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        res = last = 0
        for x, y in sorted(zip(growTime, plantTime), reverse=True):
            last += y
            res = max(res, last + x)
        
        return res