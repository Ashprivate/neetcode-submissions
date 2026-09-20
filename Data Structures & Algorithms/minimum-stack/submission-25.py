class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        
    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val  

        # print(self.stack, f"min {self.min}");        

    def pop(self) -> None:
        if not self.stack:
            return None

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop   

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.min + self.stack[-1]
             
        else:
            return self.min
             

    def getMin(self) -> int:
        # print("getMin", self.min)
        return self.min