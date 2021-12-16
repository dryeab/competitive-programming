# link - https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        

    def push(self, x: int) -> None:
        self.push_stack.append(x)
        self.pop_stack = self.push_stack[::-1]
        return x
        

    def pop(self) -> int:
        ans = self.pop_stack.pop()
        self.push_stack = self.pop_stack[::-1]
        return ans

    def peek(self) -> int:
        return self.pop_stack[-1]
        
    def empty(self) -> bool:
        return len(self.pop_stack) == 0
