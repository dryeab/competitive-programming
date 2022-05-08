# link - https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# space: O(n)
# time: O(n)

def has_cycle(head):
    
    store = set()
    
    while (head):
        if head in store:
            return 1
        store.add(head)
        head = head.next
        
    return 0
