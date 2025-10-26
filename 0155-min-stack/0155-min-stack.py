class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mini = self.getMin()
        #do not use 'if not mini' because if mini is zero, 'mini' becomes false
        if mini==None or mini > val:
            mini = val
        
        self.stack.append([val, mini])
        
    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            self.stack.pop()
            print(self.stack)
            return

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()