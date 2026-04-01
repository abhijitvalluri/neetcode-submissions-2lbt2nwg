class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque()
        q.append([0, 0]) # position, steps
        res = float('inf')

        while q:
            pos, steps = q.popleft()
            if pos == len(nums) - 1:
                res = min(res, steps)
                continue

            for jump in range(1, nums[pos] + 1):
                next = pos + jump
                q.append([next, steps + 1])
        
        return res
