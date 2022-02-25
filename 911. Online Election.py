# Link - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        votes, win = Counter(), {}
        
        cur_p = None
        
        for i, person in enumerate(persons):
            
            votes[person] += 1
            
            if cur_p == None or votes[person] >= votes[cur_p]:
                cur_p = person
            
            win[times[i]] = cur_p
        
        self.win, self.times = win, times
        
    def q(self, t: int) -> int:
        
        start, end = 0, len(self.times) - 1

        while start < end:
            
            mid = (start + end)//2
            
            if self.times[mid] == t:
                return self.win[self.times[mid]]
            
            if self.times[mid] > t and (mid == 0 or self.times[mid-1] < t):
                return self.win[self.times[mid-1]]
            elif self.times[mid] > t:
                end = mid -1
            elif self.times[mid] < t and (mid == len(self.times) -1 or self.times[mid+1] > t):
                return self.win[self.times[mid]] 
            else:
                start = mid + 1
                
        return self.win[self.times[start]]
