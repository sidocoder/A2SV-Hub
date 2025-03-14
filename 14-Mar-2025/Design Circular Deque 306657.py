# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque(maxlen = k)
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.queue) ==self.k:
            return False
        self.queue.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.append(value)
        return True
    
    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            return True
        return False        

    def getFront(self) -> int:
        return self.queue[0] if self.queue else -1        

    def getRear(self) -> int:
        return self.queue[-1] if self.queue else -1
        

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False
        

    def isFull(self) -> bool:
        return len(self.queue) == self.k 
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()