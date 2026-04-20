class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, char in enumerate(senate):
            if char == 'D':
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            d, r = D.popleft(), R.popleft()

            if d < r:
                D.append(d + n)
            else:
                R.append(r + n)
        
        return 'Radiant' if R else 'Dire'
