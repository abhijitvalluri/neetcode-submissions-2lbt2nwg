class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def neighbours(combo):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(combo[:i] + digit + combo[i + 1:])
                digit = str((int(lock[i]) + 9) % 10)
                res.append(combo[:i] + digit + combo[i + 1:])
            return res

        q = deque(["0000"])
        visited = set(deadends)
        visited.add("0000")
        steps = 0

        while q:
            steps += 1
            size = len(q)
            for _ in range(size):
                combo = q.popleft()
                for nextCombo in neighbours(combo):
                    if nextCombo == target:
                        return steps
                    elif nextCombo not in visited:
                        q.append(nextCombo)
                        visited.add(nextCombo)
        
        return -1
