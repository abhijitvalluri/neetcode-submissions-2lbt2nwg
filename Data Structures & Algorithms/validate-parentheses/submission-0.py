class Solution:
    def isValid(self, s: str) -> bool:
        closingParan = {
            "(" : ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for ch in s:
            if ch in closingParan:
                stack.append(closingParan[ch])
            elif stack[-1] == ch:
                stack.pop()
            else:
                return False
        
        return not stack
        