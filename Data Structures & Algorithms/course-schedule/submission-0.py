class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            premap[course].append(pre)

        visiting = set()
        
        def dfs(course):
            if course in visiting: return False
            if premap[course] == []: return True

            visiting.add(course)
            for pre in premap[course]:
                if not dfs(pre): return False
            
            visiting.remove(course)
            premap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False

        return True