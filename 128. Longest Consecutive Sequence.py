
# Link - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        parent = {num: num for num in nums}
        size = {num: 1 for num in nums}
        
        def find(v):
            if v == parent[v]:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(v1, v2):
            
            root1, root2 = find(v1), find(v2)
            
            if root1 != root2:
                
                if size[root1] < size[root2]:
                    parent[root1] = root2
                    size[root2] += size[root1]
                else:
                    parent[root2] = root1
                    size[root1] += size[root2]
        
        for num in nums:
            if num - 1 in parent:
                union(num-1, num)
            if num + 1 in parent:
                union(num+1, num)
        
        for num in nums:
            find(num)
        
        return max(size.values())