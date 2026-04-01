class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        data = [(p, s) for p, s in zip(position, speed)]
        data.sort(reverse=True)

        stack = []

        for p, s in data:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)
            
        return len(stack)
        