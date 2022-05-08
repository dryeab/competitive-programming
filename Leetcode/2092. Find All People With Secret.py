
# Link - https://leetcode.com/problems/find-all-people-with-secret/

# Space: 
# Time:

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        graph = defaultdict(list)
        for x, y, time in meetings:
            graph[x].append((time, y))
            graph[y].append((time, x))
        
        for x in graph:
            graph[x].sort(reverse=True) # sort the meetings based on their time
        
        answer, heap = set(), [(0, 0), (0, firstPerson)]
        
        while heap:
            
            heard_at, x = heappop(heap)
            
            if x in answer: # already heard the secret before heard_at
                continue;

            answer.add(x)
            
            for time, y in graph[x]:
                if y not in answer: # if y hasn't already heard the secret
                    if time < heard_at: # time of the meeting is earlier
                        break;
                    heappush(heap, (time, y))
        
        return list(answer)