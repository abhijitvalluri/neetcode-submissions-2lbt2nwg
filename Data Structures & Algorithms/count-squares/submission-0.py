class CountSquares:

    def __init__(self):
        self.ptX = defaultdict(lambda: defaultdict(int))
        self.ptY = defaultdict(lambda: defaultdict(int))
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.ptX[x][y] += 1
        self.ptY[y][x] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        total = 0
        if x not in self.ptX and y not in self.ptY:
            return 0

        for newY in self.ptX[x]:
            if newY != y:
                side = abs(newY - y)
                if x + side in self.ptY[newY] and x + side in self.ptY[y]:
                    total += self.ptX[x][newY] * self.ptY[newY][x + side] * self.ptY[y][x + side]
                if x - side in self.ptY[newY] and x - side in self.ptY[y]:
                    total += self.ptX[x][newY] * self.ptY[newY][x - side] * self.ptY[y][x - side]
        return total
