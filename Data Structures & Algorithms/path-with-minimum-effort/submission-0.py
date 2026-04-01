class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minHeap = [(0, 0, 0)] # (diff, row, col)
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return diff
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, (newDiff, nr, nc))
        
        return -1