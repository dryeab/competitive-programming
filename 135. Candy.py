
# Link - https://leetcode.com/problems/candy/

# Space: O(n)
# Time: O(nlog(n))

class Solution:
    def candy(self, ratings: List[int]) -> int:

        candies = [0]*len(ratings)
        
        heap = [(rating, i) for i, rating in enumerate(ratings)]
        heapq.heapify(heap)
        
        while heap:
            
            rating, i = heapq.heappop(heap)
            if (i == 0 or ratings[i-1] >= ratings[i]) and (i == len(ratings)-1 or ratings[i+1] >= ratings[i]):
                # if both side has higher rating
                candies[i] = 1
            else:
                # one/two sides has less value
                M = -1
                if i:
                    if ratings[i-1] < ratings[i]:
                        M = i - 1
                        
                if i < len(ratings) - 1:
                    if ratings[i+1] < ratings[i] and \
                            (M == -1 or candies[M] < candies[i+1]):
                        M = i + 1
                
                candies[i] = candies[M] + 1
                
                # print(candies)
                
        return sum(candies)