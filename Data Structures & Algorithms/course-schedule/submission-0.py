class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        visiting = set()
        def dfs(course):
            if not prereqs[course]:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            prereqs[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True