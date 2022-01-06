# link - https://leetcode.com/problems/car-pooling/

# space: O(n)
# time: O(n)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[1])
        
        store = {} # to store how many people drop at key kms
        i = 0
        
        for num, frm, to in trips:
            while (i <= frm):
                if i in store:
                    capacity += store.pop(i)
                i += 1
            if capacity < num:
                return False
            capacity -= num
            if to in store:
                store[to] += num
            else:
                store[to] = num
        
        return True
