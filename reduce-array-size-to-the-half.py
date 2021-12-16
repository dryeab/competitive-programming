
# link - https://leetcode.com/problems/reduce-array-size-to-the-half/


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr)
        
        temp = [(y, x) for x, y in counter.items()]
        temp = sorted(temp, reverse=True)
        
        i = 0
        sum_of_freq = 0
        while (sum_of_freq < len(arr)/2):
            sum_of_freq += temp[i][0]
            i += 1
        
        return i
