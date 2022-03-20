
# Link - https://leetcode.com/problems/seat-reservation-manager/

# Space: O(n)

class SeatManager:

    def __init__(self, n: int): # Time: O(n)
        self.heap = [i+1 for i in range(n)] # store unreserved seats
        heapq.heapify(self.heap)

    def reserve(self) -> int: # Time: O(log(n))
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None: # Time: O(log(n))
        heapq.heappush(self.heap, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)