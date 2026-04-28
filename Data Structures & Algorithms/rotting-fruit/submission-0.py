class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        ROW = len(grid)
        COL = len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (0 <= row < len(grid)) and \
                       (0 <= col < len(grid[0])) and \
                       grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1