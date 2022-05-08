

# link - https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.size = 0
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None or self.stack[self.min] > val:
            self.min = len(self.stack) - 1

    def pop(self) -> None:
        ans = self.stack.pop()
        
        if not len(self.stack):
            self.min = None
            return ans
        
        self.min = self.stack.index(min(self.stack))
        return ans
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
