
# Link - https://leetcode.com/problems/dota2-senate/

# Space: O(n)
# Time: O(n)

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        k, votes = 0, list(senate)  
        
        Rs = deque([i for i in range(len(senate)) if senate[i] == 'R'])
        Ds = deque([i for i in range(len(senate)) if senate[i] == 'D'])
        
        while Ds or Rs:
            
            if votes[k]:
                if votes[k] == 'R':

                    if not Ds:
                        return 'Radiant'

                    votes[Ds.popleft()] = None
                    Rs.append(Rs.popleft())

                else:

                    if not Rs:
                        return 'Dire'

                    votes[Rs.popleft()] = None
                    Ds.append(Ds.popleft())
            
            k = (k + 1)%len(senate)