class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        node = ListNode(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.size = 0
            self.head = None
            self.tail = None
            return True
        
        oldHead = self.head
        self.head = self.head.next
        self.head.prev = None
        oldHead.next = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        
        return self.tail.val
        
    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()