class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = []
        visited = set()
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: continue
                if (r, c) not in visited:
                    stack.append((r, c))
                    visited.add((r, c))
                    area = 1
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            row = x + dx
                            col = y + dy
                            if (row, col) in visited: continue
                            if (row in range(len(grid)) and col in range(len(grid[0])) and \
                               grid[row][col] == 1):
                                stack.append((row, col))
                                visited.add((row, col))
                                area += 1
                    
                    maxArea = max(maxArea, area)
        
        return maxArea


