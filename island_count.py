class Solution:

    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, curr_row, curr_col, nrows, ncols):
        return 0 <= curr_row < nrows and 0 <= curr_col < ncols

    def bfs(self, grid, i, j, visited, dx, dy, nrows, ncols,L):
        visited[i][j] = True
        #print(visited)
        q = []
        q.append((i,j))
        while len(q) > 0:
            curr_row, curr_col = q.pop(0)
            for i in range(len(dx)):
                next_row = curr_row + dy[i]
                next_col = curr_col + dx[i]
                if self.is_valid(next_row, next_col, nrows, ncols) and not visited[next_row][next_col]:
                    visited[next_row][next_col]=True
                    #print(visited)
                    # 1 means we encounter land, lets save it
                    if grid[next_row][next_col]==1:
                        q.append((next_row, next_col))
                        #size+=1
                        L[0]=L[0]+1
                        print(L,id(L))
                        #print(size)
        return

    def island_count(self, grid):

        """ given a grid of 1 and 0 where 0 means water and 1 means land, find count of islands.
         Here island means continuous piece of land surrounded by water. We can move in 8 directions shown by dy and dx.
         example grid = [[1,1,0,0],[0,0,1,1]] has count as 2.
         Essentially we record how many times BFS is called, means we encounter a 1(land). Value is stored in cnt."""


        nrows = len(grid)
        ncols = len(grid[0])
        visited = [[False] * ncols for _ in range(nrows)]
        cnt = 0
        # use maxsize to get size of the largest island, (same as count of 1's in an island)
        maxsize = -9999
        #size = 0
        L=[]
        # define directios of motion, left right, up, down, southeast, northeast, northwest, southwest
        dx = [-1, 1, 0, 0,1,1,-1,-1 ]
        dy = [0, 0, -1, 1, 1,-1,-1,1]
        for i in range(nrows):
            for j in range(ncols):
                if not visited[i][j] and grid[i][j]==1:
                    #size=1
                    L.append(1)
                    print(L,id(L))
                    self.bfs(grid, i, j, visited, dx, dy, nrows, ncols,L)
                   # print(visited)
                    cnt+=1
                    print(L,id(L))
                    maxsize=max(maxsize, L[0])
                    L=[]
                    #print(maxsize)
        return cnt,maxsize


obj = Solution([[1,1,0,0],[0,0,1,1],[1,0,1,1],[1,0,0,0]])
result,res = obj.island_count([[1,1,0,0],[0,0,1,1],[1,0,1,1],[1,0,0,0]])