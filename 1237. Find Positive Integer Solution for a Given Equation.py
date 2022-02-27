
# Link - https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

# Solution 1
    # Space: ~
    # Time: O(x + y)

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        ans, f, x = [], customfunction.f, 1000
        
        for i in range(1, 1001):
            while x and f(x, i) > z:
                x -= 1
            if x and f(x, i) == z:
                ans.append((x,i))
        
        return ans

# Space: ~
# Time: O(x*log(y))

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        ans, f = [], customfunction.f
        
        # the smallest possible value of x
        start, end = 1, 1000
        while start < end:
            mid = (start + end)//2
            val = f(mid, 1000)
            
            if val >= z:
                end = mid
            else:
                start = mid + 1
                
        start_x = start
        
        for x in range(start_x, 1001):
            
            start, end = 1, 1000
            while start < end:
                mid = (start + end)//2
                val = f(x,mid)
                if val == z:
                    ans.append([x,mid])
                    break;
                if val >= z:
                    end = mid
                else:
                    start = mid + 1
                    
        return ans