class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if self.stack[-1] > 0:
            self.stack.pop()
        else:
            self.min -= self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        return self.min + (self.stack[-1] if self.stack[-1] > 0 else 0)

    def getMin(self) -> int:
        return self.min
