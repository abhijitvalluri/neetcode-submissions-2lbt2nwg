class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        num_asteriods = len(asteroids)
        i = 0

        while i < num_asteriods:
            a = asteroids[i]
            if not stack or (a > 0 or stack[-1] < 0):
                stack.append(a)
                i += 1
            else:
                top = stack[-1]
                if abs(top) > abs(a):
                    i += 1
                elif abs(top) < abs(a):
                    stack.pop()
                else:
                    stack.pop()
                    i += 1
            
        return stack
        