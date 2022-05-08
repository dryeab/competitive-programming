
# Link - https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

# Space: O(n)
# Time: O(n)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        answer, store = [], defaultdict(list)
        
        for i, size in enumerate(groupSizes):
            
            store[size].append(i)
            
            if len(store[size]) == size:
                answer.append(store[size])
                store[size] = []
        
        return answer