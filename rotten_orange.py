class Solution:
    def __init__(self):
        pass

    def valid (self, row, col, nrows, ncols):
        return 0 <= row < nrows and 0 <= col < ncols

    def good_orange (self,row,col,grid):
        return grid[row][col]==1

    def bfs(self, grid, q, visited, time, dx, dy, fresh_cnt, nrows, ncols):

        while len(q) > 0 and fresh_cnt > 0:

            m = len(q)
            #print(q, fresh_cnt,m)


            for i in range(m):
                elem = q.pop(0)
                for j in range(len(dx)):
                    newrow = elem[0]+dy[j]
                    newcol = elem[1]+dx[j]
                    if self.valid(newrow,newcol,nrows,ncols):
                        #print(q,m,"hello",fresh_cnt,(newrow,newcol),elem,len(q),time)
                        if self.good_orange(newrow,newcol,grid) and not visited[newrow][newcol]:
                            #print(q,grid[newrow][newcol])
                            visited[newrow][newcol]=True
                            q.append((newrow,newcol))
                            fresh_cnt-=1

            if fresh_cnt > 0 and len(q) == 0:
                return -1
            time+=1
        return time



    def rotten_main(self, grid):
        """ Given a grid, where each cell has one of following values;
        0: empty cell,
        1: cell has fresh orange, and
        2: cell has rotten oranges.
        Determine the minimum time by which all oranges will be rotten.
        Note: We can move in four directions; up, down, left, and right.

        Idea: Use multisource BFS, i.e. maintain a queue of all rotten oranges at a given time, and
        perform BFS only on that list of rotten oranges. And also maintain count of fresh oranges left. """

        nrows = len(grid)
        ncols = len(grid[0])
        q = []
        fresh_cnt = 0
        visited = [[False] * ncols for _ in range(nrows)]
        time = 0
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
        return self.bfs(grid, q, visited, time, dx, dy, fresh_cnt,nrows,ncols)

if __name__=="__main__":
    obj = Solution()
    res = obj.rotten_main([[1,2,0],[0,1,2],[0,1,1]])