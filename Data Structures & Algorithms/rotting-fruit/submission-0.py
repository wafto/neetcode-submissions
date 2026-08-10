class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neightbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    continue
                if grid[r][c] == 1:
                    fresh.add((r, c))
            
        if not fresh:
            return 0

        elapsed = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in neightbors:
                    rx = r + nr
                    cx = c + nc
                    if rx >= 0 and cx >= 0 and rx < rows and cx < cols and grid[rx][cx] == 1:
                        queue.append((rx, cx))
                        fresh.remove((rx, cx))
                        grid[rx][cx] = 2
            elapsed += 1
        
        return elapsed if not fresh else -1

