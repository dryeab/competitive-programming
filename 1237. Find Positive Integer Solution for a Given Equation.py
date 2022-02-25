
# Link - https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

# Space: ~
# Time: O(n*log(n))

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        f = customfunction.f
        
        ans = []
        
        """
        1, find the value of x (with y=1000) which gives above z
        2, find the value of y for each x ( from step 1) which gives z
            - y may not be available
            - y can exist (only one y exist for a given x)
        """
        
        # find the smallest value of x
        start, end = 1, 1000
        while start < end:
            mid = (start + end)//2
            val = f(mid, 1000)
            
            if val >= z:
                end = mid
            else:
                start = mid + 1
        
        # found the starting point of x which
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
                    
#             if f(x, start) == z:
#                 ans.append([x, mid])
                
        return ans
