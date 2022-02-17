
# link - https://leetcode.com/problems/lru-cache/

# space: O(n)
# time: O(1) (get & put)

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val # value of the key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.tail = None
        self.store = {}
        
    def get(self, key: int) -> int:
        # print('get', key, self.store)
        if key in self.store:
            
            node = self.store[key]
            
            if node != self.head:
            
                if node == self.tail:
                    self.tail = node.prev
                    self.tail.next = None

                else:

                    # connect the two (before and after)
                    node.prev.next = node.next
                    node.next.prev = node.prev

                # change the position of the recently used node to head of the list
                node.prev = None
                node.next = self.head
                self.head.prev = node
                
                self.head = node
            
            return node.val
        
        return -1
    
    def addAtHead(self, key, value):
        
        if self.head == None:
            self.tail = self.head = Node(key, value)
        else:
            self.head.prev = Node(key, value, None, self.head)
            self.head = self.head.prev
            # self.tail.next = Node(key, value, self.tail, None)
            # self.tail = self.tail.next
            
        self.store[key] = self.head
        
    def put(self, key: int, value: int) -> None:
        
        # print('put', key, value, self.store)
        
        if key in self.store:
            node = self.store[key]
            node.val = value
            self.get(key)
        else:
            if len(self.store) == self.capacity:
                
                self.store.pop(self.tail.key)
                
                self.tail.key = key
                self.tail.val = value
                
                self.store[key] = self.tail
                
                self.get(key)
            else:
                self.addAtHead(key, value)
