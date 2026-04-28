class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c):
            if (r < 0 or len(grid) <= r or c < 0 or len(grid[0]) <= c or
             grid[r][c] == '0' or (r, c) in visited):
                return 0
            visited.add((r, c))
            for dx, dy in directions:
                row = r + dx
                col = c + dy
                dfs(row, col)
            return 1


        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += dfs(row, col)

        return count


