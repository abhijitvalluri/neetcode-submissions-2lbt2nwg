class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        othersTrust = defaultdict(int)
        selfTrust = defaultdict(int)
        candidate = -1
        for t in trust:
            othersTrust[t[1]] += 1
            selfTrust[t[0]] += 1

            if candidate == -1:
                if othersTrust[t[1]] == n - 1 and selfTrust[t[1]] == 0:
                    candidate = t[1]
            elif selfTrust[candidate] != 0:
                return -1
            
        return candidate
        