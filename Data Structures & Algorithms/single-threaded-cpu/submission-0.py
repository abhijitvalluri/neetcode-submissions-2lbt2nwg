class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskHeap = []
        for i, task in enumerate(tasks):
            heapq.heappush(taskHeap, (task[0], task[1], i))
        
        res, availTasks, time = [], [], 0
        while taskHeap or availTasks:
            while taskHeap and taskHeap[0][0] <= time:
                _, procTime, idx = heapq.heappop(taskHeap)
                heapq.heappush(availTasks, (procTime, idx))
            
            if not availTasks:
                time = taskHeap[0][0]
            else:
                procTime, idx = heapq.heappop(availTasks)
                res.append(idx)
                time += procTime

        return res
