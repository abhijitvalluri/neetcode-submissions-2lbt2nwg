class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totSum = sum(nums)
        if totSum % k != 0:
            return False

        nums.sort(reverse=True)
        partitions = [0] * k
        target = totSum // k

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if partitions[j] + nums[i] > target:
                    continue
                
                partitions[j] += nums[i]
                if dfs(i+1):
                    return True
                
                partitions[j] -= nums[i]
                if partitions[j] == 0:
                    break
            
            return False
        
        return dfs(0)
