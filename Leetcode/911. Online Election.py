# Link - https://leetcode.com/problems/online-election/

# Space: O(n)
# Time:
    # __init__: O(n)
    # q: O(log(n))

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        leader, votes, win = None, Counter(), {}

        for i, person in enumerate(persons):
            
            votes[person] += 1
            
            if leader == None or votes[person] >= votes[leader]:
                leader = person
            
            win[times[i]] = leader
        
        self.win, self.times = win, times
        
    def q(self, t: int) -> int:
        
        left, right = 0, len(self.times) - 1
        
        while left < right:
            
            mid = (left + right)//2
            
            if self.times[mid] <= t:
                left = mid + 1
            else:
                right = mid

        if self.times[left] > t:
            left -= 1
        
        return self.win[self.times[left]]