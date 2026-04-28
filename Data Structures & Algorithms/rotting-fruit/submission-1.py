class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = set()
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: fresh.add((r, c))
                if grid[r][c] == 2: q.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while len(fresh) > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dx, dy in directions:
                    row = r + dx
                    col = c + dy
                    if (row, col) in fresh:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh.remove((row, col))

            time += 1
        

        return time if len(fresh) == 0 else -1