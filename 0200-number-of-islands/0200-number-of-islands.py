class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] = '0'
                    stack = [r * COLS + c]
                    
                    while stack:
                        pos = stack.pop()
                        curr_r = pos // COLS
                        curr_c = pos % COLS
                        
                        if curr_r > 0 and grid[curr_r - 1][curr_c] == '1':
                            grid[curr_r - 1][curr_c] = '0'
                            stack.append((curr_r - 1) * COLS + curr_c)
                        if curr_r < ROWS - 1 and grid[curr_r + 1][curr_c] == '1':
                            grid[curr_r + 1][curr_c] = '0'
                            stack.append((curr_r + 1) * COLS + curr_c)
                        if curr_c > 0 and grid[curr_r][curr_c - 1] == '1':
                            grid[curr_r][curr_c - 1] = '0'
                            stack.append(curr_r * COLS + (curr_c - 1))
                        if curr_c < COLS - 1 and grid[curr_r][curr_c + 1] == '1':
                            grid[curr_r][curr_c + 1] = '0'
                            stack.append(curr_r * COLS + (curr_c + 1))
                                
        return islands

