class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curMin = self.stack[-1][1] if self.stack else float("inf")
        newMin = min(val, curMin)
        self.stack.append((val, newMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
