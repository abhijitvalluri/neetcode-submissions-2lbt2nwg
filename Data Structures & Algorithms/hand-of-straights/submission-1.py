class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for num in hand:
            start = num
            while counts[start - 1]:
                start -= 1
            while start <= num:
                while counts[start]:
                    for i in range(start, start + groupSize):
                        if counts[i] == 0:
                            return False
                        counts[i] -= 1
                start += 1
            
        return True
        