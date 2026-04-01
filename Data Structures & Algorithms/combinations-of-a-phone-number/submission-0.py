class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        t9map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []

        def backtrack(i, partial):
            if i == len(digits):
                res.append("".join(partial))
                return
            
            dig = digits[i]
            chars = t9map[dig]
            for char in chars:
                partial.append(char)
                backtrack(i + 1, partial)
                partial.pop()
        
        backtrack(0, [])
        return res
        