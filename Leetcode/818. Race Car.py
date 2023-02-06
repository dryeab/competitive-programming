class Solution:
    def racecar(self, target: int) -> int:
        
        q, visited = deque([(0, 1)]), set([(0, 1)]) # pos, speed
        
        res = 0
        while q:
            for _ in range(len(q)):
                pos, speed = q.popleft()
                if pos == target:
                    return res
                A = (pos + speed, speed * 2)
                R = (pos, -1 if speed > 0 else 1)
                if A not in visited and 0 <= A[0] <= 2 * target:
                    q.append(A)
                    visited.add(A)
                if R not in visited:
                    q.append(R)
                    visited.add(R)
            res += 1
        
        return -1