class Solution:

    def __init__(self, grid):
        self.grid = grid

    def valid_cell(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] != 0

    def identify_source(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        src_row, src_col = -1, -1
        for i in range(nrows):
            for j in range(ncols):
                # find source location
                if grid[i][j] == 1:
                    src_row = i
                    src_col = j
                    break
        if src_row == -1:
            return False
        visited = [[False] * ncols for _ in range(nrows)]
        #print(src_row, src_col, visited)
        return src_row, src_col, visited

    def path_helper(self, grid, row, col, visited):
        if grid[row][col] == 2:
            return True
        visited[row][col] = True
        dx = [0, 0, - 1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(len(dx)):
            new_row = row + dx[i]

            new_col = col + dy[i]
            if self.valid_cell(grid, new_row, new_col) and visited[new_row][new_col] == False:
                if self.path_helper(grid, new_row, new_col, visited):
                    return True

        return False

    def path_validator(self, grid):
        if self.identify_source(grid)==False:
            return False
        src_row, src_col, visited = self.identify_source(grid)
        return self.path_helper(grid, src_row, src_col, visited)

obj = Solution([[1, 3, 0, 0], [3, 3, 3, 0], [0, 3, 3, 3], [0, 0, 0, 2]])
result = obj.path_validator([[1, 3, 0, 0], [3, 3, 3, 0], [0, 3, 3, 3], [0, 0, 0, 2]])




