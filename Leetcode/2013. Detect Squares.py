class DetectSquares:
    def __init__(self):
        self.xp = defaultdict(list)
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xp[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.xp[x1]:
            if y2 == y1: continue 
            sl = abs(y2 - y1)

            x3, y3 = x1 - sl, y2
            x4, y4 = x1 - sl, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            x3, y3 = x1 + sl, y2
            x4, y4 = x1 + sl, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans