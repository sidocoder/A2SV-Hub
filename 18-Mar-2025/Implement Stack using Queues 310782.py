# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.Stack = deque()        

    def push(self, x: int) -> None:
        self.Stack.append(x)        

    def pop(self) -> int:
        if self.Stack:
            removed = self.Stack.pop()
            return removed
        return False        

    def top(self) -> int:
        if self.Stack:
            return self.Stack[-1]
        return False        

    def empty(self) -> bool:
        if self.Stack:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()