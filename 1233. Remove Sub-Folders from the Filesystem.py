
# Link - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

# Solution 1
    # Space: O(n)
    # Time: O(nlog(n) + m*n)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        heapq.heapify(folder) # O(m*n)
        answer = [heapq.heappop(folder)] # n
        
        while folder: # O(nlog(n))
            f = heapq.heappop(folder)
            n = len(answer[-1])
            if f[:n] != answer[-1] or f[n] != '/':
                answer.append(f)
        
        return answer


# Solution 2
    # Space: O(n)
    # Time: (m^2 * n)
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        c_folder = set(folder)
        
        for f in folder:
            for j in range(1, len(f)):
                if f[j] == '/':
                    if f[:j] in c_folder:
                        c_folder.remove(f)
                        break
        
        return list(c_folder)