class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefixStack or val < self.prefixStack[-1]:
            self.prefixStack.append(val)
        else:
            self.prefixStack.append(self.prefixStack[-1])

    def pop(self) -> None:
        self.prefixStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixStack[-1]