class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.lruHead = None
        self.lruTail = None
    
    def moveToFront(self, node) -> None:
        if node == self.lruTail: # Already at the front
            return
        
        if node == self.lruHead:
            self.lruHead = node.next
            self.lruHead.prev = None
            node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = sel.lruTail
            
        node.prev = self.lruTail
        self.lruTail.next = node
        self.lruTail = node


    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        
        node = self.keyMap[key]
        self.moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.moveToFront(node)
        else:
            node = Node(key, value)
            self.keyMap[key] = node
            if not self.lruTail: # First node
                self.lruHead = node
                self.lruTail = node
            else:
                self.lruTail.next = node
                node.prev = self.lruTail
                self.lruTail = node
                if len(self.keyMap) > self.capacity:
                    oldHead = self.lruHead
                    self.lruHead = oldHead.next
                    self.lruHead.prev = None
                    oldHead.next = None
                    del self.keyMap[oldHead.key]
        
