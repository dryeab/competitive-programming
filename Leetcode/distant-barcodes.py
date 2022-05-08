# link - https://leetcode.com/problems/distant-barcodes/submissions/

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        from collections import Counter
        
        freq_counter = [(y, x) for x, y in Counter(barcodes).items()] # the number of times each item occurred
        freq_counter = sorted(freq_counter, reverse=True) # sort them based on their frequency
        
        result = [None] * len(barcodes) # to store the final result
        i = 0
        for freq, num in freq_counter:
            for _ in range(freq):
                result[i] = num
                i += 2
                if i >= len(barcodes):
                    i = 1
                    
        return result
