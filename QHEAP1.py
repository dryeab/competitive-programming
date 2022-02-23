
# Link - https://www.hackerrank.com/challenges/qheap1/problem

from heapq import *

heap, removed = [], set()

Q = int(input())

for _ in range(Q):
    
    r = input()
    
    if r == '3':
        while heap[0] in removed:
            heappop(heap)
        print(heap[0])
        
    elif r[0] == '1':
        
        val = int(r[2:])
        if val in removed:
            removed.remove(val)
        heappush(heap, val)
        
    else:
        
        val = int(r[2:])
        
        removed.add(val)
