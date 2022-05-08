

# link - https://leetcode.com/problems/design-circular-deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.front = []
        self.last = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front.append(value)
        self.last = self.front[::-1]
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.last.append(value)
        self.front = self.last[::-1]
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front.pop()
        self.last = self.front[::-1]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.last.pop()
        self.front = self.last[::-1]
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front[-1]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last[-1]

    def isEmpty(self) -> bool:
        return len(self.front) == 0

    def isFull(self) -> bool:
        return len(self.front) == self.k
