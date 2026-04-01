class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values:
            return ""
        
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp and (mid + 1 > r or values[mid + 1][0] > timestamp):
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return "" 
