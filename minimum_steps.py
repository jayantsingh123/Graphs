class Solution:

    def __init__(self, grid):
        self.grid = grid

    def is_valid_cell(self, grid,  row, col, nrows, ncols):
        return 0 <= row < nrows and 0 <= col < ncols and grid[row][col] == 1


    def minimum_steps_in_a_grid(self, grid) -> int:
        """ find minimum number of steps to go from
        cell (0,0) of the grid to cell (n-1, m-1)
        where the grid is size n x m
        cell with 0 is unwalkable
        cell with 1 is walkable
        Idea: using Breadth First Search to traverse all neighbors first for a cell.
        Then traverse neighbors of each neighbor"""


        nrows = len(grid)
        ncols = len(grid[0])
        visited = [[False] * ncols for _ in range(nrows)]
        q = []
        q.append((0, 0, 0))
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while len(q) > 0:
            (curr_row, curr_col, curr_steps) = q.pop(0)
            if curr_row == nrows-1 and curr_col == ncols-1:
                # reached  the destination
                return curr_steps
            for i in range(len(dx)):
                new_row = curr_row + dx[i]
                new_col = curr_col + dy[i]
                if self.is_valid_cell(grid, new_row, new_col, nrows, ncols):
                    if not visited[new_row][new_col]:
                        q.append((new_row, new_col, curr_steps+1))
                        visited[new_row][new_col] = True
        return -1

obj = Solution([[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1]])
result = obj.minimum_steps_in_a_grid([[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1]])