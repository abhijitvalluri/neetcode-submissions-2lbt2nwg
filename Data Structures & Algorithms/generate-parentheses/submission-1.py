class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openBrack, closedBrack):
            if openBrack == closedBrack == n:
                res.append("".join(stack))
                return
            
            if openBrack < n:
                stack.append("(")
                backtrack(openBrack + 1, closedBrack)
                stack.pop()
            if closedBrack < openBrack:
                stack.append(")")
                backtrack(openBrack, closedBrack + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
