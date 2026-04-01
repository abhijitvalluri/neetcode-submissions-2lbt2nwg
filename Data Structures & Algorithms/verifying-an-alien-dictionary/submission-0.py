class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {ch: idx for idx, ch in enumerate(order)}

        def compare(word):
            return tuple(order_index[ch] for ch in word)
        
        return words == sorted(words, key=compare)
        