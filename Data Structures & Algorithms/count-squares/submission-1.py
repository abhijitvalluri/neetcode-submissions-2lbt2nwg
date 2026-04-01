class CountSquares:

    def __init__(self):
        self.pts = defaultdict(lambda: defaultdict(int))
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        total = 0
        for newY in self.pts[x]:
            if newY != y:
                side = abs(newY - y)
                total += self.pts[x][newY] * self.pts[x + side][newY] * self.pts[x + side][y]
                total += self.pts[x][newY] * self.pts[x - side][newY] * self.pts[x - side][y]
        return total
