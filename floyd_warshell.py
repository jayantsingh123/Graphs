class Solution:
    def __init__(self):
        pass
    def floyd(self, grid):
        n = len(grid[0])
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])
        return grid
if __name__=="__main__":
    obj = Solution()
    res = obj.floyd([[0,2,float('inf'),5,float('inf')],
                     [float('inf'),0,float('inf'),float('inf'),6],
                     [float('inf'),float('inf'),0,float('inf'),1],
                     [float('inf'),float('inf'),2,0,float('inf')],
                     [float('inf'),float('inf'),float('inf'),7,0]])