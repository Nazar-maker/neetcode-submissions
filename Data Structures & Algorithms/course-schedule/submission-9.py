class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            preMap[u].append(v)

        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            if not preMap[node]:
                return True

            visited.add(node)
            for n in preMap[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True
