class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac = set()
        atl = set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r<0 or c<0 or r==len(heights) or c==len(heights[0]) or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            for dx, dy in directions:
                dfs(r+dx, c+dy, visit, heights[r][c])
        
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights)-1, c, atl, heights[len(heights)-1][c])

        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0])-1, atl, heights[r][len(heights[0])-1])

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row, col])

        return res
