class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.stacks = []

    def push(self, val: int) -> None:
        self.counts[val] += 1
        if self.counts[val] > len(self.stacks):
            stack = [val]
            self.stacks.append(stack)
        else:
            self.stacks[self.counts[val] - 1].append(val)

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.counts[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()