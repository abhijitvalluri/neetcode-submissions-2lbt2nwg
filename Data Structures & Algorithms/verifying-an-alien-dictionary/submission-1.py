class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {ch: idx for idx, ch in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
            return True

    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        order_index = {ch: idx for idx, ch in enumerate(order)}

        def compare(word):
            return tuple(order_index[ch] for ch in word)
        
        return words == sorted(words, key=compare)
        