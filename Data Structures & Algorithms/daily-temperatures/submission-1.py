class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                oldIdx, oldTemp = stack.pop()
                result[oldIdx] = index - oldIdx

            stack.append((index, temp))

        return result
       