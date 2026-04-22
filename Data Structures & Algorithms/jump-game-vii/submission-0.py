class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        n = len(s)
        visited = 0

        while q:
            pos = q.popleft()
            start = max(pos + minJump, visited + 1)
            for i in range(start, min(pos + maxJump + 1, n)):
                if s[i] == '0':
                    if i == n - 1:
                        return True
                    q.append(i)
            
            visited = pos + maxJump
        
        return False
