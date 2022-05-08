
# link - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            node = self.head
            for i in range(index):
                node = node.next
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, None, self.head)
        if self.size == 0:
            self.tail = self.head = node
        else:
            self.head.prev = node
            self.head = node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail, None)
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            if index == self.size:
                self.addAtTail(val)
            elif index == 0:
                self.addAtHead(val)
            else:
                node = self.head
                for i in range(index):
                    node = node.next
                new_node = Node(val, node.prev, node)
                node.prev.next = new_node
                node.prev = new_node
                
                # print('add', new_node.prev.val, new_node.val, new_node.next.val)
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if self.size == 1:
                self.head = self.tail = None
            else:
                node = self.head
                for i in range(index):
                    node = node.next
                    
                if node == self.head:
                    self.head = node.next
                    self.head.prev = None
                elif node == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    
            self.size -= 1
